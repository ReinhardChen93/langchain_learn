"""
常见的索引类型：

  索引类型	  适用场景	              内存占用	  精度	    构建速度
  FLAT	    小数据精确搜索（<100万）	   高	      100%	      快
  IVF_FLAT	大数据平衡场景（千万级）	    中	    95%-98%	    较快
  HNSW	    高召回率需求	              高	    98%-99%	    慢
  DISKANN	  超大规模（10亿+）	          低	    90%-95%	    最慢
"""

# 使用MilvusClient（推荐的新API）
from pymilvus import MilvusClient, DataType

# 实例化MilvusClient以连接到指定的Milvus服务器
client = MilvusClient(
    uri="http://127.0.0.1:19530"
)

# 使用MilvusClient API列出数据库
databases = client.list_databases()
print(f'Available databases (MilvusClient): {databases}')

# 使用特定数据库
client.use_database("my_database")

# 索引操作示例
# 创建schema对象，设置自动ID生成和动态字段特性
schema = MilvusClient.create_schema(
    auto_id=False,
    enable_dynamic_field=True,
)

# 向schema中添加字段"id"，数据类型为INT64，作为主键
schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
# 向schema中添加字段"vector"，数据类型为FLOAT_VECTOR，维度为5
schema.add_field(field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=5)

# 使用create_collection方法根据schema创建集合"customized_setup"
client.create_collection(
    collection_name="customized_setup", 
    schema=schema, 
)
 
# 准备索引参数，为"vector"字段创建索引
index_params = MilvusClient.prepare_index_params()

# 添加索引配置，指定字段名、度量类型、索引类型、索引名和参数
index_params.add_index(
    field_name="vector",
    metric_type="COSINE", # 距离计算方式 (L2/IP/COSINE)
    index_type="IVF_FLAT",
    index_name="vector_index", 
    params={ "nlist": 128 }  #聚类中心数 (建议值：sqrt(数据量))
)

# 创建索引，不等待索引创建完成即返回
client.create_index(
    collection_name="customized_setup",
    index_params=index_params,
    sync=False # 是否等待索引创建完成后再返回。默认为True。
)

# 最佳实践避坑指南
"""
1. 连接管理:
   - 使用MilvusClient API或ORM API时保持一致，避免混用导致连接问题
   - 长时间运行的应用应定期检查连接状态

2. 索引选择:
   - 小数据集(<100万)：使用FLAT获取精确结果
   - 中等数据集(千万级)：使用IVF_FLAT平衡性能和精度
   - 高精度需求：使用HNSW获得高召回率
   - 超大数据集：考虑DISKANN节省内存

3. 索引参数调优:
   - IVF_FLAT: nlist ≈ sqrt(向量数) * 4
   - HNSW: M(边数)=16~64, efConstruction=40~400 (值越大精度越高但构建越慢)

4. 内存管理:
   - 搜索前必须加载集合(load_collection)
   - 不用时释放集合(release_collection)避免内存溢出

5. 批量操作:
   - 插入数据时使用批量插入(batch_size=1000~5000)提高效率
   - 搜索时合并多个查询为批量搜索减少网络开销

6. 分区策略:
   - 按时间、类别等维度创建分区提高查询效率
   - 搜索时只加载相关分区节省内存

7. 避坑提示:
   - 向量维度创建后不可更改，设计时要考虑未来需求
   - 大批量数据导入前先估算存储和内存需求
   - 生产环境使用前务必进行性能测试和调优
"""