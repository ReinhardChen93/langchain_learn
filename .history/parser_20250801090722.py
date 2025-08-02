from langchain_core.output_parsers import CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

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

print(final_prompt.to_messages())