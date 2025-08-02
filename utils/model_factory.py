from langchain_openai import ChatOpenAI
from utils.config import get_model_config, update_model_config
from typing import Dict, Any, Optional

class ModelFactory:
    """模型工厂类，用于动态创建和管理模型实例"""
    
    def __init__(self):
        self._models: Dict[str, ChatOpenAI] = {}
    
    def create_model(self, model_name: str, **override_params) -> ChatOpenAI:
        """
        创建模型实例
        
        Args:
            model_name: 模型名称
            **override_params: 覆盖默认参数
            
        Returns:
            ChatOpenAI实例
        """
        # 获取基础配置
        config = get_model_config(model_name)
        
        # 应用覆盖参数
        config.update(override_params)
        
        # 创建模型实例
        model = ChatOpenAI(**config)
        
        # 缓存模型实例
        self._models[model_name] = model
        
        return model
    
    def get_model(self, model_name: str, **override_params) -> ChatOpenAI:
        """
        获取模型实例（如果已存在则返回缓存的实例）
        
        Args:
            model_name: 模型名称
            **override_params: 覆盖参数（仅在创建新实例时使用）
            
        Returns:
            ChatOpenAI实例
        """
        if model_name in self._models and not override_params:
            return self._models[model_name]
        
        return self.create_model(model_name, **override_params)
    
    def update_model_config(self, model_name: str, **kwargs) -> None:
        """更新模型配置"""
        update_model_config(model_name, **kwargs)
        
        # 如果模型已缓存，清除缓存以使用新配置
        if model_name in self._models:
            del self._models[model_name]
    
    def list_models(self) -> list:
        """列出所有可用的模型名称"""
        from utils.config import MODEL_CONFIGS
        return list(MODEL_CONFIGS.keys())
    
    def get_model_info(self, model_name: str) -> Dict[str, Any]:
        """获取模型信息"""
        return get_model_config(model_name)

# 创建全局模型工厂实例
model_factory = ModelFactory()

# 便捷函数
def get_model(model_name: str, **kwargs) -> ChatOpenAI:
    """获取模型实例的便捷函数"""
    return model_factory.get_model(model_name, **kwargs)

def create_model(model_name: str, **kwargs) -> ChatOpenAI:
    """创建新模型实例的便捷函数"""
    return model_factory.create_model(model_name, **kwargs) 