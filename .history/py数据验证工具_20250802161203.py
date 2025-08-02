from py数据验证工具 import BaseModel

# 类似java中的POJO ，但getter setter 方法是自动生成的
class User(BaseModel):
    name: str
    age: int
    email: str
# 创建一个User对象
user = User(name="Alice", age=30, email="<EMAIL>")
# 打印User对象的属性
print(user.name)  # 输出: Alice
print(user.age)   # 输出: 30
print(user.email) # 输出: <EMAIL>