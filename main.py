from llm import llm
from retriever import get_relevant_docs
from prompt_utils import build_prompt

def ask_question(question):
    try:
        # 관련 문서 검색
        docs = get_relevant_docs(question)
        if not docs:
            return "관련 문서를 찾을 수 없습니다."

        context = "\n".join([doc.page_content for doc in docs])

        # 프롬프트 구성
        prompt = build_prompt(context, question)

        # 답변 생성
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"에러 발생: {e}"

if __name__ == "__main__":
    print("💬 NutriMatch 챗봇에 오신 걸 환영합니다!")
    print("종료하려면 'exit' 또는 'quit'를 입력하세요.\n")

    while True:
        user_input = input("❓ 질문을 입력하세요: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 종료합니다.")
            break
        answer = ask_question(user_input)
        print(f"\n🤖 답변: {answer}\n")
