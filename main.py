# main.py

from llm import get_llm
from vector_store import create_vectorstore_from_texts
from retriever import get_retriever

# 예시용 텍스트 (과제용)
texts = [
    "고혈압에는 나트륨 섭취를 줄이고 칼륨이 많은 식품을 섭취해야 합니다.",
    "칼륨이 많은 음식으로는 바나나, 시금치, 아보카도 등이 있습니다.",
    "운동과 식이요법은 고혈압 관리에 중요합니다."
]

# 벡터스토어 생성 및 검색기 생성
vectorstore = create_vectorstore_from_texts(texts)
retriever = get_retriever(vectorstore)

# LLM 연결
llm = get_llm()

# 사용자 질문
query = input("질문을 입력하세요: ")

# 문서 검색 + 답변 생성
docs = retriever.get_relevant_documents(query)
context = "\n".join([doc.page_content for doc in docs])

prompt = f"""너는 건강 상담 전문가야. 아래 문서를 참고해서 질문에 답변해줘.

[문서]
{context}

[질문]
{query}

[답변]"""

response = llm.predict(prompt)
print("\n📢 답변:", response)
