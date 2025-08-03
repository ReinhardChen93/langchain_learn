"""
如何提取PDF里面的图片文案？

PyPDFLoader 仅提取文本，如果没配置第三方类库则会提取不了对应的图片文案

需结合其他库（如camelot、pdfplumber、rapidocr-onnxruntime）提取表格或图像。

如果需要提取，安装好依赖库后，设置extract_images参数为True。
"""

# 安装依赖包 pip install rapidocr-onnxruntime
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("data/pdf-img.pdf", extract_images=True)
pages = loader.load()
print(pages[0].page_content)