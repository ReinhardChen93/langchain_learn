from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser, JsonOutputParser
import os

API_KEY = os.environ.get("YUANJING_API_KEY")

# Initialize the output parser
output_parser = JsonOutputParser()

# 定义系统提示模板
system_message = SystemMessagePromptTemplate.from_template("""
    回答以下问题，返回 JSON 格式：  
    {{  
        "answer": "答案文本",  
        "confidence": 置信度（0-1）  
    }}  
    问题：{question}   
    """)
# 定义用户提示模板
user_message = HumanMessagePromptTemplate.from_template("请回答以下问题：{question}")

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])

# 初始化聊天模型
chat_model = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
    api_key=API_KEY,
    temperature=0.7,  
)

chain = chat_prompt | chat_model | output_parser
# 使用链式调用
response = chain.invoke({"question": "什么是人工智能？"})
print(response)