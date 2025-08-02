from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os

API_KEY = os.environ.get("YUANJING_API_KEY")

# 创建模型
model =OpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
  api_key=API_KEY,
  temperature=0.7
)

# 创建一个 PromptTemplate 对象
prompt_template = PromptTemplate(
  input_variables=["input_text"],
  template="为{input_text}生成三个押韵的广告词。"
)

prompt_text = prompt_template.format(input_text="手机")
print(prompt_text)
# 使用模型生成广告词

# response = model.invoke(prompt_text)
# # 打印生成的广告词
# print(response)