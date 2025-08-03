from langchain_community.document_loaders import PyPDFLoader
# PDF加载
loader = PyPDFLoader("data/test.pdf")
# 加载文档并按页分割
pages = loader.load()  # 返回 Document 对象列表

# 查看页数
print(f"总页数: {len(pages)}")

# 访问第一页内容
page_content = pages[0].page_content
metadata = pages[0].metadata
print(f"第一页内容:\n{page_content[:200]}...")  # 预览前200字符
print(f"元数据: {metadata}")

# 加载指定页码范围（例如第2页到第4页）
pages = loader.load([1, 2, 3])  # 注意页码从0开始（第1页对应索引0）

# 提取所有文本合并为单个文档,  若需将全部页面内容合并为一个字符串：
full_text = "\n\n".join([page.page_content for page in pages])
print(f"合并后的全文长度: {len(full_text)} 字符")

# 文本分块不理想

# 调整分块策略：选择合适的分隔符或分块大小

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", "."],  # 按段落、句子分割
    chunk_size=500,
    chunk_overlap=100
)

# 批量处理PDF：遍历文件夹内所有PDF文件。
import os
pdf_folder = "data/"
all_pages = []
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, filename))
        all_pages.extend(loader.load())