from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os

API_KEY = os.environ.get("YUANJING_API_KEY")


# 创建系统提示词
system_message = SystemMessagePromptTemplate.from_template("""  
  你是一位{domain}.
  请将歌词翻译成{lang}语言。
  """)

# 创建用户提示词
user_message = HumanMessagePromptTemplate.from_template("请帮我翻译{text}的歌词")

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])

# 定义输出解析器
output_parser = StrOutputParser()

# 定义输入变量
input_variables = {
    "domain": "歌词翻译专家",
    "lang": "中文",
    "text": "just the two of us",
}

# 使用聊天提示模板和输入变量生成最终的提示词
prompt = chat_prompt.format_prompt(**input_variables)



# 创建语言模型
model = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
    api_key=API_KEY,
    temperature=0.7,
    streaming=True
)

# 调用语言模型生成响应
chain = chat_prompt | model | output_parser

# 流式输出
print(chain.invoke(input_variables))
