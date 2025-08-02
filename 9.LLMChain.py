from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
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

# 定义用户消息
user_message = HumanMessagePromptTemplate.from_template("请回答：{question}")

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])

# 定义输入变量
input_variables = {
    "domain": "医学",
    "lang": "中文",
    "style": "简洁",
    "question": "什么是癌症？"
}

# 创建 LLMChain
chain = LLMChain(llm=model, prompt=chat_prompt)
# 运行链
result = chain.run(input_variables)
# 打印结果
print(result)