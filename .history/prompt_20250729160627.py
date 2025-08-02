from langchain.prompts import PromptTemplate

# 定义模板  
template = """  
你是一位专业的{domain}顾问，请用{language}回答：  
问题：{question}  
回答：  
""" 