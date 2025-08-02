from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
API_KEY = os.environ.get("YUANJING_API_KEY")

# 创建提示词模版
prompt = ChatPromptTemplate.from_template(
    input_variables=["input_language", "output_language", "text"],
    template="""
    You are a helpful assistant that translates {input_language} to {output_language}.
    Translate the following text to {output_language}: {text}
    """
)

# 定义输入变量
input_variables = {
    "input_language": "English",
    "output_language": "Chinese",
    "text": "Hello, how are you?"
}

# 创建输出解析器  
output_parser = CommaSeparatedListOutputParser()

# 使用提示词模版和输入变量生成提示词
prompt_text = prompt.format(**input_variables)

# 创建语言模型
model = ChatOpenAI(
    model="qwen2.5-72b-instruct",
    base_url="https://maas-api.ai-yuanjing.com/openapi/compatible-mode/v1",
    api_key=API_KEY,
    temperature=0.7,
    streaming=True
)

# 调用语言模型生成响应
chain = prompt_text | model | output_parser



# 打印解析后的响应
