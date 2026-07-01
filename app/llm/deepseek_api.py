from langchain_deepseek import ChatDeepSeek


model = ChatDeepSeek(
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    api_key="sk-b5eb2d64fbc449c7b6c0c7eea58002e9",
    temperature=0,
    max_retries=3 
)

