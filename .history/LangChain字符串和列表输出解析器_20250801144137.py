from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

# 创建提示词模版
prompt = PromptTemplate(
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
# 打印生成的提示词
print(prompt_text)