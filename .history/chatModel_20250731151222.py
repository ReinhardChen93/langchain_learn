from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import os

API_KEY = os.environ.get("YUANJING_API_KEY")

# 创建模型
model = ChatOpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
  api_key=API_KEY,
  temperature=0.7
)

# 定义系统消息
system_message = SystemMessagePromptTemplate.from_template("你是一位{domain}专家，请用{lang}语言回答。回答需要满足：{style}。")

#用户消息模版
user_message = HumanMessagePromptTemplate.from_template("请解释：{question}")

# 组合聊天信息模版
chat_template = ChatPromptTemplate.from_messages([
    system_message,
    user_message
])

chat_template.format(
    domain="机器学习",
    lang="中文",
    style="简单",
    question="机器学习是什么？"
)

response = model.invoke(chat_template)

print(response)