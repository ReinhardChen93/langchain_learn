from langchain_core.output_parsers import CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os

API_KEY = os.environ.get("YUANJING_API_KEY")

# Initialize the output parser
output_parser = CommaSeparatedListOutputParser()
# 获取格式化指令
format_instructions = output_parser.get_format_instructions()
# 定义系统提示模板
system_message = SystemMessagePromptTemplate.from_template("""
  You are a helpful assistant that translates {input_language} to {output_language}.
  格式化指令: {format_instructions}
  """)
# 定义用户提示模板
user_message = HumanMessagePromptTemplate.from_template("Translate the following text to {output_language}: {text}")

# 定义输入变量
input_variables = {
    "input_language": "English",
    "output_language": "Chinese",
    "text": "Hello, how are you?",
    "format_instructions": format_instructions
}

# 创建聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])

#注入格式化指令
final_prompt = chat_prompt.format_prompt(**input_variables)

# 定义模型
model = ChatOpenAI(
  model="qwen2.5-72b-instruct",
  base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
  api_key=API_KEY,
  temperature=0.7,
  streaming=True
)

# 创建流式输出
stream = model.stream(final_prompt.to_messages())
for chunk in stream:
    print(chunk.content, end="", flush=True)
