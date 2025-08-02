from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
API_KEY = os.environ.get("YUANJING_API_KEY")

# 创建模型
model = ChatOpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
  api_key=API_KEY,
  temperature=0.7
)

# 定义系统消息模板
system_message = SystemMessagePromptTemplate.from_template("你是一位{domain}专家，请用{lang}语言回答。回答需要满足：{style}。")

# 用户消息模版
user_message = HumanMessagePromptTemplate.from_template("请解释：{question}")

# 组合聊天信息模版
chat_template = ChatPromptTemplate.from_messages([
    system_message,
    user_message
])

# 定义输出解析器
str_out_put_parser = StrOutputParser()

chain = chat_template | model | str_out_put_parser | RunnablePassthrough()

response = chain.invoke({
    "domain": "机器学习",
    "lang": "中文",
    "style": "简单",
    "question": "请解释机器学习"
})
# 输出结果
print(response)