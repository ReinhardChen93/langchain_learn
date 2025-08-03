"""
RecursiveCharacterTextSplitter 递归字符分割器
核心特点
  递归字符分割器采用多级分隔符优先级切割机制，是 LangChain 中使用最广泛的通用分割器。
  递归尝试多种分隔符（默认顺序：["\n\n", "\n", " ", ""]），优先按大粒度分割
  若块过大则继续尝试更细粒度分隔符，适合处理结构复杂或嵌套的文本。
核心参数说明
  from langchain.text_splitter import RecursiveCharacterTextSplitter
  splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,          # 目标块大小（字符）每个块最多包含 1000 个字符
      chunk_overlap=200,        # 块间重叠量，最多有200个字符重叠
      separators=["\n\n", "\n", "。", "？", "!", " ", ""],  # 优先级递减的分割符
      length_function=len,      # 长度计算函数
      keep_separator=True,      # 是否保留分隔符
  )
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter

paper_text = """
引言机器学习近年来取得突破性进展...（长文本）若块过大则继续尝试更细粒度分隔符，适合处理结构复杂或嵌套的文本

方法我们提出新型网络架构...（技术细节）按优先级（如段落、句子、单词）递归分割文本，优先保留自然边界,如换行符、句号

实验在ImageNet数据集上...处理技术文档时，使用chunk_size=800和chunk_overlap=100,数据表格
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=4
)
paper_chunks = splitter.split_text(paper_text)
print(len(paper_chunks))
for chunk in paper_chunks:
    print(chunk)
