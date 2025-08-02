from langchain_core.prompts import ChatPromptTemplate

# 定义消息列表，包含系统指令、用户输入和AI回复模板, 通过元组列表定义角色和模板，动态插入name和user_input变量
chat_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个助手AI，名字是{name}。"),
    ("human", "你好，最近怎么样？"),
    ("ai", "我很好，谢谢！"),
    ("human", "{user_input}")
])

# 格式化模板并传入变量
messages = chat_template.format_messages(
    name="Bob", 
    user_input="你最喜欢的编程语言是什么？"
)
print(messages)
# 输出结果示例：
# SystemMessage(content='你是一个助手AI，名字是Bob。')
# HumanMessage(content='你好，最近怎么样？')
# AIMessage(content='我很好，谢谢！')
# HumanMessage(content='你最喜欢的编程语言是什么？')

from langchain_core.prompts import (
    ChatPromptTemplate, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)

# 创建单条消息模板,通过细分模板类（如SystemMessagePromptTemplate）定义单条消息，再通过from_messages组合
system_template = SystemMessagePromptTemplate.from_template(
    "你是一个{role}，请用{language}回答。"
)
user_template = HumanMessagePromptTemplate.from_template("{question}")

# 组合成多轮对话模板
chat_template = ChatPromptTemplate.from_messages([
    system_template,
    user_template
])

# 使用示例
messages = chat_template.format_messages(
    role="翻译助手", 
    language="中文",
    question="将'I love Python'翻译成中文。"
)
print(messages)

# 输出结果示例：
# SystemMessage(content='你是一个翻译助手，请用中文回答。')
# HumanMessage(content='将'I love Python'翻译成中文。')