import os
from langchain_openai import ChatOpenAI
from langchain_core.tracers.langchain import LangChainTracer
from dotenv import load_dotenv

load_dotenv()

# LangSmith 연동 설정
tracer = LangChainTracer(project_name="school-project")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# OpenAI 연결
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
)
llm.callback_manager = tracer
