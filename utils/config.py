import os
from typing import Dict, Any

# 模型配置
MODEL_CONFIGS = {
    "unicn": {
        "model": "Qwen3-235B-A22B",
        "base_url": "http://10.186.2.176:10010/CUCCAI-llm-hub",
        "api_key": os.environ.get("UNICN_API_KEY", "850cbd86-e83f-42c5-8fbe-96f1e43753ae"),
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
        "api_key": os.environ.get("YUANJING_API_KEY"),
        "temperature": 0.7,
        "streaming": False,
        "max_tokens": 1000,
        "top_p": 0.8,
        "frequency_penalty": 0.1,
        "presence_penalty": 0.1
    },
    "openai": {
        "model": "gpt-3.5-turbo",
        "base_url": "https://api.openai.com/v1",
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "temperature": 0.5,
        "streaming": True,
        "max_tokens": 1500,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
}

def get_model_config(model_name: str) -> Dict[str, Any]:
    """获取指定模型的配置"""
    if model_name not in MODEL_CONFIGS:
        raise ValueError(f"未知的模型名称: {model_name}")
    return MODEL_CONFIGS[model_name].copy()

def update_model_config(model_name: str, **kwargs) -> None:
    """更新模型配置"""
    if model_name not in MODEL_CONFIGS:
        raise ValueError(f"未知的模型名称: {model_name}")
    MODEL_CONFIGS[model_name].update(kwargs) 