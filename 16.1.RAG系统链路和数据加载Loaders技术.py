from langchain_community.document_loaders import TextLoader, UnstructuredMarkdownLoader, CSVLoader, JSONLoader
# 加载文本文件
loader = TextLoader("data/sample.txt", encoding="utf-8")
# markdownLoader = UnstructuredMarkdownLoader("data/sample.md", encoding="utf-8")
csvLoader = CSVLoader("data/云南省前5级行政区划_2023.csv", encoding="utf-8")
documents = loader.load()
# md_documents = markdownLoader.load()
csv_documents = csvLoader.load()

print(f"加载的文档数量: {len(documents)}")
print(f"文档内容: {documents[0].page_content}") # 获取文档内容  page_content[100] 前100个字符
print(f"文档元数据: {documents[0].metadata}")
# print(f"Markdown文档数量: {len(md_documents)}")
# print(f"Markdown文档内容: {md_documents[0].page_content}")
# print(f"Markdown文档元数据: {md_documents[0].metadata}")
print(f"CSV文档数量: {len(csv_documents)}")
print(f"CSV文档内容: {csv_documents[0].page_content[100]}")
