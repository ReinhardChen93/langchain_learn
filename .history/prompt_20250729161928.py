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


template = """
分析用户情绪（默认分析类型： {analyze_type}）：
用户输入: {input_text}
分析结果：
"""

prompt_template = PromptTemplate(
  input_variables=["input_text"],
  template=template,
  partial_variables={"analyze_type": "sentiment"} #固定值
)

print(prompt_template.format(input_text="我今天心情很好！"))