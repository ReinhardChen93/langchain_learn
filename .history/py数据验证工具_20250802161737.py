from pydantic import BaseModel

# 类似java中的POJO ，但getter setter 方法是自动生成的
class User(BaseModel):
    name: str
    age: int
    email: str | None = None  # 可选字段，默认为None
# 创建一个User对象
user = User(name="Alice", age=30, email="<EMAIL>")
# 打印User对象的属性
print(user.name)  # 输出: Alice
print(user.age)   # 输出: 30
print(user.email) # 输出: <EMAIL>

#创建实例化与校验
try:
  User(name = "Bob", age = 25, email = "bob@example.com")
except ValueError as e:
  print(f'Error: {e.errors()}')