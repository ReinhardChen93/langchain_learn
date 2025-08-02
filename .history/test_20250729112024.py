# 执⾏简单测试
from langchain_core.prompts import ChatPromptTemplate
print(ChatPromptTemplate.from_template("Hello 欢迎来到⼩滴课堂-AI⼤模型开发课程{title}!").format(title=",⼲就完了"))
# 应输出: Human: Hello 欢迎来到⼩滴课堂-AI⼤模型开发课程 ,⼲就完了!
import os

from langchain_openai import ChatOpenAI

# 设置环境变量
API_KEY = os.environ.get("YUANJING_API_KEY")
llm = ChatOpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1/chat/completions",
  api_key=API_KEY,
  temperature=0.7
  )

llm.invoke("请写一个关于机器学习的文章")
