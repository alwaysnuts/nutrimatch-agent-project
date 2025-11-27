import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langsmith import Client
from langchain_core.tracers import ConsoleCallbackHandler, LangChainTracer

# 환경변수 로드
load_dotenv()

# LangSmith 설정
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"

# LangSmith 트레이서 설정
tracer = LangChainTracer(project_name="nutrimatch-school")

# LLM 설정 (LangSmith 추적 가능)
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    callbacks=[tracer, ConsoleCallbackHandler()]
)
