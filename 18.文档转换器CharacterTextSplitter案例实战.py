"""
核心特点

是 LangChain 中最基础的文本分割器，采用固定长度字符切割策略。

适用于结构规整、格式统一的文本处理场景，强调精确控制块长度

适用于结构清晰的文本（如段落分隔明确的文档）。

核心参数详解

参数	类型	默认值	说明
separator	str	"\n\n"	切割文本的分隔符
chunk_size	int	4000	每个块的最大字符数
chunk_overlap	int	200	相邻块的重叠字符数
strip_whitespace	bool	True	是否清除块首尾空格
is_separator_regex	bool	False	是否启用正则表达式分隔符


适合场景
  推荐使用：
    结构化日志处理
    代码文件解析
    已知明确分隔符的文本（如Markdown）
    需要精确控制块大小的场景
  不推荐使用：
    自然语言段落（建议用RecursiveCharacterSplitter）
    需要保持语义完整性的场景
    包含复杂嵌套结构的文本
"""
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
loader = TextLoader('data/sample.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(
  separator="\n",
  chunk_size=500,
  chunk_overlap=10
)
chunks = text_splitter.split_documents(documents)
print(f"分块数量: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk.page_content)
    print("-" * 40)
