"""
简介：大模型修复机制OutputFixingParser解析器

OutputFixingParser

是LangChain中用于修复语言模型（LLM）输出格式错误的工具，通常与PydanticOutputParser配合使用。

当原始解析器因格式问题（如JSON语法错误、字段缺失等）失败时，它能自动调用LLM修正输出，提升解析的鲁棒性。

核心功能：

  自动纠错：修复不规范的输出格式（如单引号JSON、字段顺序错误等）。

  兼容性：与Pydantic数据模型无缝集成，支持结构化输出验证。

  容错机制：避免因模型输出不稳定导致程序中断
"""

from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from utils.model_factory import get_model, create_model
from typing import List

# 创建模型
model = get_model("yuanjing")
# 创建修复模型
fixModel = create_model(
  "yuanjing",
  model="deepseek-r1"
)

# 创建Pydantic模型
class Actor(BaseModel):
  name: str = Field(description="演员姓名")
  film_titles: List[str] = Field(default_factory=list, description="参演电影列表")
  
# 创建Pydantic输出解析器
output_parser = PydanticOutputParser(pydantic_object=Actor)

# 创建提示模板
prompt_template = PromptTemplate(
  template="{format_instructions}\n请列出以下演员的参演电影：{question}", # 提示模板
  input_variables=["question"], # 输入变量
  partial_variables={
    "format_instructions": output_parser.get_format_instructions() # 格式化说明
  }
)

# 包装输出修复解析器
fixing_parser = OutputFixingParser.from_llm(
  parser=output_parser, # 输出解析器
  llm=fixModel # 修复模型
  )
# 使用修复解析器和模型创建链
chain = prompt_template | model | fixing_parser
# 调用链
response = chain.invoke({"question": "汤姆哈迪"})
print(response)
print(type(response))
print(response.model_dump_json())
