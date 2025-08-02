"""
模型参数管理使用示例
"""

# 方式1：使用配置文件
from utils.config import get_model_config, update_model_config
from langchain_openai import ChatOpenAI

print("=== 方式1：使用配置文件 ===")
# 获取配置并创建模型
config = get_model_config("yuanjing")
model1 = ChatOpenAI(**config)

# 动态更新配置
update_model_config("yuanjing", temperature=0.9, max_tokens=2000)
config_updated = get_model_config("yuanjing")
model1_updated = ChatOpenAI(**config_updated)

# 方式2：使用模型工厂
from utils.model_factory import get_model, create_model

print("\n=== 方式2：使用模型工厂 ===")
# 获取默认模型
model2 = get_model("yuanjing")

# 创建带自定义参数的模型
model2_custom = create_model("yuanjing", temperature=0.5, streaming=True)

# 方式3：使用utils/model.py
from utils.model import create_model as utils_create_model, update_model_config as utils_update_config

print("\n=== 方式3：使用utils/model.py ===")
# 创建模型
model3 = utils_create_model("yuanjing")

# 更新配置
utils_update_config("yuanjing", temperature=0.3)

# 创建新模型（使用更新后的配置）
model3_new = utils_create_model("yuanjing")

# 实际使用示例
print("\n=== 实际使用示例 ===")

# 示例1：不同温度设置
model_cool = create_model("yuanjing", temperature=0.1)  # 更保守的回答
model_creative = create_model("yuanjing", temperature=0.9)  # 更创造性的回答

# 示例2：不同token限制
model_short = create_model("yuanjing", max_tokens=100)  # 简短回答
model_long = create_model("yuanjing", max_tokens=2000)  # 详细回答

# 示例3：流式vs非流式
model_stream = create_model("yuanjing", streaming=True)  # 流式输出
model_non_stream = create_model("yuanjing", streaming=False)  # 非流式输出

# 示例4：组合参数
model_custom = create_model("yuanjing", 
                           temperature=0.7,
                           max_tokens=1500,
                           top_p=0.9,
                           frequency_penalty=0.1,
                           presence_penalty=0.1)

print("所有模型创建完成！")

# 测试调用
try:
    response = model_custom.invoke("请简单介绍一下Python")
    print(f"模型响应: {response.content[:100]}...")
except Exception as e:
    print(f"调用失败: {e}") 