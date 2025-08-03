"""
WebBaseLoader 是 LangChain 中用于抓取 静态网页内容 的文档加载器。
  通过 HTTP 请求直接获取网页 HTML，并提取其中的文本内容（自动清理标签、脚本等非文本元素）
  生成包含网页文本和元数据的 Document 对象
  适用于新闻文章、博客、文档页面等静态内容的快速提取。
场景:
  知识库构建（知识问答、企业知识库）、舆情监控（新闻/社交媒体分析）
  竞品分析（产品功能/价格监控）、SEO 内容聚合
pip install beautifulsoup4          # HTML 解析依赖（默认已包含）
pip install requests                # 网络请求依赖（默认已包含）
"""
# 加载单个网页
import os
#代码中设置USER_AGENT, 设置USER_AGENT的代码一定要放在WebBaseLoader 这个包前面，不然还是会报错
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 14.0; Win64; x64) AppleWebKit/567.36 (KHTML, like Gecko) Chrome/58.0.444.11 Safari/337.3'

from langchain_community.document_loaders import WebBaseLoader # 只可以加载静态网站
#警告日志信息：USER_AGENT environment variable not set, consider setting it to identify your requests.

# 初始化加载器，传入目标URL列表（可多个）
urls = ["https://www.cnblogs.com"]
loader = WebBaseLoader(urls)

# 加载文档（返回Document对象列表）
docs = loader.load()

# 查看结果
print(f"提取的文本长度: {len(docs[0].page_content)} 字符")
print(f"前200字符预览:\n{docs[0].page_content[:200]}...")
print(f"元数据: {docs[0].metadata}")

# 批量加载多个网页
import os
#代码中设置USER_AGENT, 注意设置USER_AGENT的代码一定要放在WebBaseLoader 这个包前面，不然还是会报错
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

from langchain_community.document_loaders import WebBaseLoader
#警告日志信息：USER_AGENT environment variable not set, consider setting it to identify your requests.

# 初始化加载器，传入目标URL列表（可多个）
urls = [
    "https://news.baidu.com/",  # 新闻
    "https://tieba.baidu.com/index.html"  # 贴吧
    
]
loader = WebBaseLoader(urls)
docs = loader.load()

print(f"共加载 {len(docs)} 个文档")
print("各文档来源:")
for doc in docs:
    print(f"- {doc.metadata['source']}")