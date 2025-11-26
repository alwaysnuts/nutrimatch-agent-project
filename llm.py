# llm.py

from langchain.chat_models import ChatOpenAI
import os
import langsmith_config  # LangSmith 연동 설정 불러오기

def get_llm():
    return ChatOpenAI(
        temperature=0.2,
        model="gpt-3.5-turbo",  # 필요시 gpt-4로 변경 가능
        streaming=True
    )
