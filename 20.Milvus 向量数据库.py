
#也可以使用MilvusClient
#from pymilvus import MilvusClient
#client = MilvusClient("http://47.119.128.20:19530")

from pymilvus import connections, db, FieldSchema, CollectionSchema, DataType, Collection
conn = connections.connect(host="127.0.0.1", port=19530)
# 创建数据库
db.create_database("my_database")
# 使用数据库
db.using_database("my_database")
# 列出数据库
dbs = db.list_database()
print(dbs)
#['default', 'my_database']
# 删除数据库
#db.drop_database("my_database")

"""
Collection与Schema的创建和管理

Collection 是一个二维表，具有固定的列和变化的行，每列代表一个字段，每行代表一个实体。

要实现这样的结构化数据管理，需要一个 Schema定义 Collections 的表结构

每个Schema由多个FieldSchema组成：
FieldSchema 定义了每个字段的名称、数据类型和其他属性。
"""
# 字段定义示例
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True), # 主键字段
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128), # 向量字段，dim为向量维度
    FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=50) # 字符串字段，max_length为最大长度
]

# 创建集合模式
schema = CollectionSchema(
  fields=fields, # 字段列表
  primary_field="id", # 主键字段
  auto_id=False, # 是否自动生成ID
  description="Example collection schema", # 描述信息
  enable_dynamic_field=True # 启用动态字段
)

# 实例化集合
collection = Collection(
  name="my_collection", # 集合名称
  schema=schema, # 集合模式
  shards_num=2 # 分片数，创建后不可更改
)