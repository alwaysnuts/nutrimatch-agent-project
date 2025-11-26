from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from langsmith import Client

# 환경변수에서 API 키 불러오기
openai_api_key = os.getenv("OPENAI_API_KEY")
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")

# LangSmith 추적 설정
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key
os.environ["LANGCHAIN_PROJECT"] = "school-project"  # LangSmith 내 프로젝트 이름

# LangSmith 클라이언트 연결
client = Client(api_key=langsmith_api_key)

# OpenAI 모델 설정
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=openai_api_key
)

# 기본 챗봇 흐름
def run_chat():
    while True:
        q = input("질문: ")
        if q.lower() in ["exit", "quit"]:
            break
        response = llm([HumanMessage(content=q)])
        print("응답:", response.content)

if __name__ == "__main__":
    run_chat()
