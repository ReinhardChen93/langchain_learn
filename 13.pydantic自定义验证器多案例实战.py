from pydantic import BaseModel, field_validator, Field
# field_validator 装饰器,用于定义自定义验证器

# 定义一个模型
class User(BaseModel):
  username: str
  nickname: str
  # 带默认值的可选参数
  age: int | None = Field(default= None, description="年龄", ge=18, le=100)

  @field_validator("username", "nickname") # 可以同时验证多个字段
  def validate_username(cls, v) -> str:
    # cls 表示类本身,v 表示要验证的值
    if len(v) < 3:
      raise ValueError("用户名长度不能小于3")
    elif v.isdigit():
      raise ValueError("用户名不能是数字")
    elif "admin" in v:
      raise ValueError("用户名不能包含admin")
    return v # 必须要返回验证后的值

  @field_validator("age")
  def validate_age(cls, v):
    if v < 18:
      raise ValueError("年龄不能小于18")
    return v
  
# 创建一个实例
user1 = User(username="张三", age=20)

# 验证数据
try:
  user1 = User(username="张三", age=15)
  print(user1)
except Exception as e:
  print(e.errors())

# 输出:
# 15 <class 'ValueError'>: 年龄不能小于18
# [ErrorDetail(type='value_error', msg='年龄不能小于18', loc=('age',))]
