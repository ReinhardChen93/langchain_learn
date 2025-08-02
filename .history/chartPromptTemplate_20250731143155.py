from langchain_core.prompts import ChatPromptTemplate

# 定义消息列表，包含系统指令、用户输入和AI回复模板, 通过元组列表定义角色和模板，动态插入name和user_input变量
chat_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个助手AI，名字是{name}。"),
    ("human", "你好，最近怎么样？"),
    ("ai", "我很好，谢谢！"),
    ("human", "{user_input}")
])

# 格式化模板并传入变量
messages = chat_template.format_messages(
    name="Bob", 
    user_input="你最喜欢的编程语言是什么？"
)
print(messages)
# 输出结果示例：
# SystemMessage(content='你是一个助手AI，名字是Bob。')
# HumanMessage(content='你好，最近怎么样？')
# AIMessage(content='我很好，谢谢！')
# HumanMessage(content='你最喜欢的编程语言是什么？')