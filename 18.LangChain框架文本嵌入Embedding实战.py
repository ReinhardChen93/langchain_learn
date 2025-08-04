"""
通过标准化接口集成了多种嵌入模型，支持开发者灵活调用

功能：对接各类文本嵌入模型的标准化接口

作用：将文本转换为向量，供后续检索/比较使用

类比：不同品牌手机充电器 → LangChain是万能充电头
"""

# 使用新的推荐导入方式
from langchain_openai import OpenAIEmbeddings
import os
from openai import OpenAI

API_KEY = os.environ.get("UNICN_API_KEY")

# 直接使用OpenAI客户端而不是LangChain包装器
try:
    # 方法1：直接使用OpenAI客户端
    client = OpenAI(
        api_key=API_KEY,
        base_url="http://10.186.2.176:10010/CUCCAI-llm-hub/v1"
    )
    
    # 示例文本
    comments = [
        "这个手机性能不错，但是价格有点贵",
        "这个手机性能不错，但是屏幕分辨率有点小",
        "这个手机性能不错，但是没有摄像头",
        "这个手机性能不错，但是没有蓝牙",
        "这个手机性能不错，但是没有Wi-Fi"
    ]
    
    # 直接调用embeddings API
    response = client.embeddings.create(
        model="Qwen3-Embedding-4B",
        input=comments
    )
    
    # 提取嵌入向量
    embeddings = [item.embedding for item in response.data]
    print(f"方法一，成功生成嵌入向量，第一个向量的前5个元素: {embeddings[0][:5]}")
    print(f"向量维度: {len(embeddings[0])}")
    
except Exception as e:
    print(f"方法1失败: {e}")
    
    try:
        # 方法2：尝试使用LangChain的OpenAIEmbeddings，但修改参数
        embedding_model = OpenAIEmbeddings(
            model="Qwen3-Embedding-4B",
            base_url="http://10.186.2.176:10010/CUCCAI-llm-hub/v1",
            api_key=API_KEY,
            max_retries=5
        )
        
        embeddings = embedding_model.embed_documents(comments)
        print(f"方法二，成功生成嵌入向量，第一个向量的前5个元素: {embeddings[0][:5]}")
        print(f"向量维度: {len(embeddings[0])}")
        
    except Exception as e:
        print(f"方法2失败: {e}")
        
        # 方法3：尝试不同的API路径
        try:
            client = OpenAI(
                api_key=API_KEY,
                base_url="http://10.186.2.176:10010/CUCCAI-llm-hub"  # 不带/v1
            )
            
            response = client.embeddings.create(
                model="Qwen3-Embedding-4B",
                input=comments
            )
            
            embeddings = [item.embedding for item in response.data]
            print(f"方法三，成功生成嵌入向量，第一个向量的前5个元素: {embeddings[0][:5]}")
            print(f"向量维度: {len(embeddings[0])}")
            
        except Exception as e:
            print(f"方法3失败: {e}")
            
            # 打印更多调试信息
            import requests
            try:
                # 检查API是否可访问
                response = requests.get("http://10.186.2.176:10010/CUCCAI-llm-hub")
                print(f"API端点测试结果: {response.status_code}")
                print(f"API响应内容: {response.text[:200]}...")
                
                # 尝试获取API支持的模型列表
                models_response = requests.get("http://10.186.2.176:10010/CUCCAI-llm-hub/v1/models", 
                                             headers={"Authorization": f"Bearer {API_KEY}"})
                print(f"模型列表API响应: {models_response.status_code}")
                print(f"模型列表: {models_response.text[:500]}...")
            except Exception as e:
                print(f"API测试失败: {e}")