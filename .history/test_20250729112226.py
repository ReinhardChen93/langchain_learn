
import os

from langchain_openai import ChatOpenAI

# 设置环境变量
API_KEY = os.environ.get("YUANJING_API_KEY")
llm = ChatOpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
  api_key=API_KEY,
  temperature=0.7
  )

llm.invoke("请写一个关于机器学习的文章")
