from pydantic import BaseModel, HttpUrl, ValidationError

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
  
class WebSite(BaseModel):
    name: str
    url: HttpUrl  # 使用HttpUrl类型进行URL验证
    visits: int = 0  # 默认访问量为0
    tags: list[str] = []  # 默认标签为空列表
# 创建一个WebSite对象
website = WebSite(name="My Site", url="https://example.com", visits=100, tags=["blog", "tech"])
# 打印WebSite对象的属性
print(website.name)  # 输出: My Site
print(website.url)   # 输出: https://example.com
print(website.visits)  # 输出: 100
print(website.tags)  # 输出: ['blog', 'tech']
# 创建一个WebSite对象，并验证URL
try:
    website = WebSite(name="My Site", url="https://example.com", visits=100, tags=["blog", "tech"])
    print(website.url)  # 输出: https://example.com
except ValidationError as e:
    print(f"Error: {e.errors()}")

# 从JSON 自动解析
class Item(BaseModel):
    name: str
    url: HttpUrl
    visits: int
    tags: list[str]
    
data = '{"name": "My Site", "url": "https://example.com", "visits": 100, "tags": ["blog", "tech"]}'
item = Item.model_validate_json(data)
# 打印解析后的对象
print(item.name)  # 输出: My Site
print(item.url)   # 输出: https://example.com
print(item.visits)  # 输出: 100
print(item.tags)  # 输出: ['blog', 'tech']  
# 导出为字典 （类似js的JSON）
item_dict = item.model_dump()
print(item_dict)  # 输出: {'name': 'My Site', 'url': 'https://example.com', 'visits': 100, 'tags': ['blog', 'tech']}