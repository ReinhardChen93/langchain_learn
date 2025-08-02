from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os

API_KEY = os.environ.get("YUANJING_API_KEY")


# 创建系统提示词
system_message = SystemMessagePromptTemplate.from_template("""  
  你是一位{domain},请将用户提问的歌词按照一行{input_language}一行{output_language}的方式输出。
  只需要输出歌词内容，不需要其他任何内容。
  格式化指令: {format_instructions}
  """)

# 创建用户提示词
user_message = HumanMessagePromptTemplate.from_template("请帮我翻译{text}的歌词")

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])

# 获取格式化指令
format_instructions = StrOutputParser().get_format_instructions()

# 定义输入变量
input_variables = {
    "domain": "歌词翻译专家",
    "input_language": "中文",
    "output_language": "英文",
    "text": "just the two of us",
    "format_instructions": format_instructions
}
# 使用聊天提示模板和输入变量生成最终的提示词
prompt = chat_prompt.format_prompt(**input_variables)

# 定义输出解析器
output_parser = CommaSeparatedListOutputParser()

# 创建语言模型
model = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
    api_key=API_KEY,
    temperature=0.7,
    streaming=True
)

# 调用语言模型生成响应
chain = prompt | model | output_parser

# 流式输出
for chunk in chain.stream(input_variables):
  print(chunk.content, end="", flush=True) #打印解析后的响应
