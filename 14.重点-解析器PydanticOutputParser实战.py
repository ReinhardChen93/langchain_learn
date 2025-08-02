"""
大模型信息输出提取（  PydanticOutputParser 结合Pydantic模型验证输出）
"""
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from utils.model_factory import get_model, create_model
from pydantic import BaseModel, Field
# 创建模型
model = get_model("yuanjing")

# 创建Pydantic模型
class Person(BaseModel):
    name: str = Field(...,description="姓名")
    age: int = Field(description="年龄", gt=0, le=100)
    gender: str = Field(description="性别")
    hobbies: list[str] = Field(default_factory=list, description="爱好")
    

# 创建解析器
parser = PydanticOutputParser(pydantic_object=Person)

# 创建系统提示词
system_prompt = SystemMessagePromptTemplate.from_template("你是一位{domain}专家，请用{lang}语言回答。回答需要满足：{style}。必须遵守：{format_instructions}")

# 创建用户提示词
user_prompt = HumanMessagePromptTemplate.from_template("请解释：{question}")

# 创建提示词
prompt = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

prompt = prompt.partial(
    domain="心理学", 
    lang="中文", 
    style="简洁",
    format_instructions=parser.get_format_instructions()
    )

chain = prompt | model | parser

response = chain.invoke("我的名字叫ReinhardChen，年龄25岁，性别男，爱好编程、阅读和旅行。请帮我提取这些信息。")
print(response)

""" 
电商评论情感分析系统（JsonOutputParser和pydantic结合）
    JsonOutputParser与PydanticOutputParser类似
    新版才支持从pydantic获取约束模型，该参数并非强制要求，而是可选的增强功能
    JsonOutputParser可以处理流式返回的部分JSON对象。
"""

from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

model = get_model("yuanjing")

# 创建pydantic模型
class SentimentResult(BaseModel):
    sentiment: str = Field(..., description="情感分析结果")
    confidence: float = Field(..., description="情感分析置信度", ge=0.0, le=1.0)
    keyWords: list[str] = Field(default_factory=list, description="关键词列表")


# 创建JsonOutputParser
json_parser = JsonOutputParser(pydantic_object=SentimentResult)
# 构建处理链  
parser = JsonOutputParser(pydantic_object=SentimentResult)  

prompt = ChatPromptTemplate.from_template(
    """  
        分析评论情感：  
        {input}  
        按以下JSON格式返回：  
        {format_instructions}  
    """
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | model | parser

# 执行分析  
result = chain.invoke({"input": "物流很慢，包装破损严重"})
print(result)
