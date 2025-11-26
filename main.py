from llm import llm
from retriever import get_relevant_docs
from prompt_utils import build_prompt

def ask_question(question):
    # 관련 문서 검색
    docs = get_relevant_docs(question)
    context = "\n".join([doc.page_content for doc in docs])

    # 프롬프트 구성
    prompt = build_prompt(context, question)

    # 답변 생성
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    while True:
        user_input = input("질문을 입력하세요: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_question(user_input)
        print(f"\n🤖 답변: {answer}\n")
