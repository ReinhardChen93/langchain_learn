import requests
import json
from typing import List, Dict, Optional, Union, Any
from dataclasses import dataclass
from enum import Enum
import time


class RoleType(Enum):
    """消息角色枚举"""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class ToolChoiceType(Enum):
    """工具选择模式枚举"""
    AUTO = "auto"
    NONE = "none"


class FinishReason(Enum):
    """结束原因枚举"""
    STOP = "stop"
    LENGTH = "length"
    TOOL_CALLS = "tool_calls"
    CONTENT_FILTER = "content_filter"


@dataclass
class Message:
    """消息结构"""
    role: str
    content: str
    name: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result = {"role": self.role, "content": self.content}
        if self.name:
            result["name"] = self.name
        return result


@dataclass
class FunctionParameter:
    """函数参数结构"""
    name: str
    description: str
    parameters: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }


@dataclass
class ToolCall:
    """工具调用结构"""
    id: str
    type: str
    function: Dict[str, Any]


@dataclass
class Choice:
    """选择结构"""
    index: int
    message: Dict[str, Any]
    logprobs: Optional[Dict[str, Any]]
    finish_reason: str


@dataclass
class Usage:
    """使用统计结构"""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class ChatResponse:
    """聊天响应结构"""
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ChatResponse':
        return cls(
            id=data["id"],
            object=data["object"],
            created=data["created"],
            model=data["model"],
            choices=[Choice(**choice) for choice in data["choices"]],
            usage=Usage(**data["usage"])
        )


class HTTPClient:
    """HTTP请求客户端"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.example.com/v1"):
        """
        初始化客户端
        
        Args:
            api_key: API密钥
            base_url: 基础URL
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        # 设置默认请求头
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
            'Accept': 'application/json'
        })
    
    def _validate_messages(self, messages: List[Message]) -> None:
        """验证消息列表"""
        if not messages:
            raise ValueError("messages不能为空")
        
        for msg in messages:
            if not isinstance(msg, Message):
                raise ValueError("messages中的元素必须是Message对象")
            if msg.role not in [role.value for role in RoleType]:
                raise ValueError(f"无效的角色类型: {msg.role}")
            if not msg.content:
                raise ValueError("消息内容不能为空")
    
    def _validate_tools(self, tools: Optional[List[FunctionParameter]]) -> None:
        """验证工具列表"""
        if tools is not None:
            for tool in tools:
                if not isinstance(tool, FunctionParameter):
                    raise ValueError("tools中的元素必须是FunctionParameter对象")
    
    def chat_completion(
        self,
        model: str,
        messages: List[Message],
        tools: Optional[List[FunctionParameter]] = None,
        tool_choice: Optional[str] = None,
        stream: bool = False,
        timeout: int = 30
    ) -> Union[ChatResponse, requests.Response]:
        """
        发送聊天完成请求
        
        Args:
            model: 模型名称
            messages: 对话历史消息列表
            tools: 可供模型调用的工具列表
            tool_choice: 工具选择模式
            stream: 是否流式返回
            timeout: 请求超时时间
            
        Returns:
            非流式：ChatResponse对象
            流式：requests.Response对象
        """
        # 参数验证
        if not model:
            raise ValueError("model不能为空")
        
        self._validate_messages(messages)
        self._validate_tools(tools)
        
        if tool_choice and tool_choice not in [choice.value for choice in ToolChoiceType]:
            raise ValueError(f"无效的tool_choice: {tool_choice}")
        
        # 构建请求数据
        data = {
            "model": model,
            "messages": [msg.to_dict() for msg in messages],
            "stream": stream
        }
        
        if tools:
            data["tools"] = [tool.to_dict() for tool in tools]
        
        if tool_choice:
            data["tool_choice"] = tool_choice
        
        # 发送请求
        url = f"{self.base_url}/chat/completions"
        
        try:
            if stream:
                # 流式请求
                response = self.session.post(
                    url,
                    json=data,
                    timeout=timeout,
                    stream=True
                )
                response.raise_for_status()
                return response
            else:
                # 非流式请求
                response = self.session.post(
                    url,
                    json=data,
                    timeout=timeout
                )
                response.raise_for_status()
                
                # 解析响应
                response_data = response.json()
                return ChatResponse.from_dict(response_data)
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"请求失败: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"响应解析失败: {str(e)}")
    
    def stream_chat_completion(
        self,
        model: str,
        messages: List[Message],
        tools: Optional[List[FunctionParameter]] = None,
        tool_choice: Optional[str] = None,
        timeout: int = 30
    ):
        """
        流式聊天完成（生成器方法）
        
        Args:
            model: 模型名称
            messages: 对话历史消息列表
            tools: 可供模型调用的工具列表
            tool_choice: 工具选择模式
            timeout: 请求超时时间
            
        Yields:
            流式响应数据
        """
        response = self.chat_completion(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
            stream=True,
            timeout=timeout
        )
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data = line[6:]  # 移除 'data: ' 前缀
                    if data == '[DONE]':
                        break
                    try:
                        yield json.loads(data)
                    except json.JSONDecodeError:
                        continue


# 使用示例
def example_usage():
    """使用示例"""
    # 初始化客户端
    client = HTTPClient(
        api_key="your-api-key-here",
        base_url="https://api.example.com/v1"
    )
    
    # 创建消息
    messages = [
        Message(role="system", content="你是一个有用的助手。"),
        Message(role="user", content="你好，请介绍一下Python。")
    ]
    
    # 非流式请求
    try:
        response = client.chat_completion(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(f"响应ID: {response.id}")
        print(f"模型: {response.model}")
        print(f"内容: {response.choices[0].message['content']}")
        print(f"Token使用: {response.usage.total_tokens}")
    except Exception as e:
        print(f"请求失败: {e}")
    
    # 流式请求
    try:
        for chunk in client.stream_chat_completion(
            model="gpt-3.5-turbo",
            messages=messages
        ):
            if 'choices' in chunk and chunk['choices']:
                content = chunk['choices'][0].get('delta', {}).get('content', '')
                if content:
                    print(content, end='', flush=True)
        print()  # 换行
    except Exception as e:
        print(f"流式请求失败: {e}")


if __name__ == "__main__":
    example_usage() 