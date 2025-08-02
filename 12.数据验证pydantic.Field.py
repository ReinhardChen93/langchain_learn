from pydantic import BaseModel, Field

# 定义一个模型
class Person(BaseModel):
    name: str = Field(..., description="姓名") # ... 表示必填,无默认值
    age: int = Field(18, description="年龄", ge=18, le=100) # 18 表示默认值,ge=18 表示年龄大于等于18,le=100 表示年龄小于等于100

# 创建一个实例
user = Person(name="张三", age=20)

# 验证数据
try:
    user = Person(name="张三", age="20")
    print(user)
except Exception as e:
    print(e.errors())