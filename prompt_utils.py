class PromptBuilder:
    def __init__(self):
        pass

    def build(self, question, docs):
        context = "\n".join(docs)
        prompt = f"""당신은 전문 영양사입니다. 아래 문서를 참고하여 질문에 답하세요.

[참고 문서]
{context}

[질문]
{question}

[답변]
"""
        return prompt
