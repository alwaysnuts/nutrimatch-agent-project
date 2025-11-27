# retriever.py
from typing import List

class DummyDoc:
    def __init__(self, page_content: str):
        self.page_content = page_content

def get_relevant_docs(question: str) -> List[DummyDoc]:
    # 검색은 하지 않고 빈 컨텍스트 반환
    return []
