def build_prompt(context, question):
    return f"""당신은 영양에 대해 잘 아는 AI입니다.

다음 문서를 참고하여 사용자 질문에 답변하세요:

[문서 내용]
{context}

[질문]
{question}

[답변]
"""
