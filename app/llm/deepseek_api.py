from langchain_deepseek import ChatDeepSeek
from app.config import api_key


model = ChatDeepSeek(
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    api_key=api_key,
    temperature=0,
    max_retries=3 
)

