# 执⾏简单测试
from langchain_core.prompts import ChatPromptTemplate
print(ChatPromptTemplate.from_template("Hello 欢迎来到⼩滴课堂-AI⼤模型开发课程{title}!").format(title=",⼲就完了"))
# 应输出: Human: Hello 欢迎来到⼩滴课堂-AI⼤模型开发课程 ,⼲就完了!