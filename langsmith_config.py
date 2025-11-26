# langsmith_config.py

import os

# LangSmith API 연동 설정
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_PROJECT"] = "school-project"  # 추적용 프로젝트명

# 선택: 로그 활성화 여부
os.environ["LANGCHAIN_TRACING_V2"] = "true"
