"""
Docx2txtLoader介绍
  是 LangChain 中专门用于加载 Microsoft Word 文档（.docx） 的文档加载器。
  提取文档中的纯文本内容（包括段落、列表、表格文字等），忽略复杂格式（如字体、颜色），生成统一的 Document 对象。
  适用于从 Word 报告中快速提取结构化文本
使用步骤
  安装依赖库
    pip install docx2txt  # 核心文本提取库
  准备.docx文件：确保目标文件为 .docx 格式（旧版 .doc 需转换），且未被加密
文档中的图片/图表未被提取
  原因：Docx2txtLoader 仅提取文本，忽略图片。
  解决：使用 python-docx 单独提取图片，也可以使用其他组件，类似OCR
"""
# 基础用法：加载单个Word文档
from langchain.document_loaders import Docx2txtLoader

# 初始化加载器，传入目标文件路径
loader = Docx2txtLoader("data/sample.docx")
documents = loader.load()
# 查看加载结果
print(f"加载的文档数量: {len(documents)}")
print(f"文档内容: {documents[0].page_content[:200]}...")
print(f"文档元数据: {documents[0].metadata}")

# 批量加载多个Word文档
import os
from langchain.document_loaders import Docx2txtLoader
# 批量加载指定目录下的所有Word文档
docx_folder = "data/docx_files/"
all_documents = []
for filename in os.listdir(docx_folder):
    if filename.endswith(".docx"):
        loader = Docx2txtLoader(os.path.join(docx_folder, filename))
        documents = loader.load()
        all_documents.extend(documents)
        print(f"加载的文档数量: {len(documents)}")

print(f"总共加载的文档数量: {len(all_documents)}")
print(f"第一个文档内容预览: {all_documents[0].page_content[:200]}...")
print(f"第一个文档元数据: {all_documents[0].metadata}")
