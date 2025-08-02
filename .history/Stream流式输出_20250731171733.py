from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os

API_KEY = os.environ.get("YUANJING_API_KEY")

# 创建模型
model = ChatOpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
  api_key=API_KEY,
  temperature=0.7,
  streaming=True
)

# 定义系统消息模板
system_message = SystemMessagePromptTemplate.from_template("你是一位{domain}专家，请用{lang}语言回答。回答需要满足：{style}。")

# 用户消息模版
user_message = HumanMessagePromptTemplate.from_template("请解释：{question}")

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])
# 创建输出解析器
output_parser = StrOutputParser()
# 创建链
chain = chat_prompt | model | output_parser
# 调用链
response = chain.stream({
    "domain": "数学",
    "lang": "中文",
    "style": "详细",
    "question": "什么是三角函数？"
})
# 打印结果
print(response) 
