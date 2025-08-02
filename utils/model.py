from langchain_openai import ChatOpenAI
import os
from typing import Dict, Any

# 基础配置
UNICN_API_KEY = os.environ.get("UNICN_API_KEY", "850cbd86-e83f-42c5-8fbe-96f1e43753ae")
YUANJING_API_KEY = os.environ.get("YUANJING_API_KEY")

# 模型配置字典
MODEL_CONFIGS = {
    "unicn": {
        "model": "Qwen3-235B-A22B",
        "base_url": "http://10.186.2.176:10010/CUCCAI-llm-hub",
        "api_key": UNICN_API_KEY,
        "temperature": 0.7,
        "streaming": True,
        "max_tokens": 2000,
        "top_p": 0.9,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    },
    "yuanjing": {
        "model": "qwen2.5-72b-instruct",
        "base_url": "https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
        "api_key": YUANJING_API_KEY,
        "temperature": 0.7,
        "streaming": False,
        "max_tokens": 1000,
        "top_p": 0.8,
        "frequency_penalty": 0.1,
        "presence_penalty": 0.1
    }
}

def create_model(model_name: str, **override_params) -> ChatOpenAI:
    """创建模型实例，支持参数覆盖"""
    if model_name not in MODEL_CONFIGS:
        raise ValueError(f"未知的模型名称: {model_name}")
    
    config = MODEL_CONFIGS[model_name].copy()
    config.update(override_params)
    
    return ChatOpenAI(**config)

def update_model_config(model_name: str, **kwargs) -> None:
    """更新模型配置"""
    if model_name not in MODEL_CONFIGS:
        raise ValueError(f"未知的模型名称: {model_name}")
    MODEL_CONFIGS[model_name].update(kwargs)

# 预创建的模型实例
model_unicn = create_model("unicn")
model_yuanjing = create_model("yuanjing")


