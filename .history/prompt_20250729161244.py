from langchain.prompts import PromptTemplate

# 定义模板  
template = """  
你是一位专业的{domain}顾问，请用{language}回答：  
问题：{question}  
回答：  
""" 
# 创建PromptTemplate对象
prompt = PromptTemplate(
    input_variables=["domain", "language", "question"],
    template=template
)
# 使用示例
domain = "心理学"
language = "中文"
question = "什么是心理健康？"
# 格式化提示
formatted_prompt = prompt.format(domain=domain, language=language, question=question)
print(formatted_prompt)

# 自动推断示例
template = "请将一下文本翻译成：{language}：{text}"
prompt = prompt.from_template(template)
formatted_prompt = prompt.format(language="英文", text="你好，世界！")
print(formatted_prompt)