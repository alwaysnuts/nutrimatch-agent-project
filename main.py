from llm import LLM
from retriever import Retriever
from prompt_utils import PromptBuilder

if __name__ == "__main__":
    retriever = Retriever()
    llm = LLM()
    prompt_builder = PromptBuilder()

    print("🧠 NutriMatch 챗봇이 시작되었습니다.")
    while True:
        query = input("질문하세요: ")
        if query.lower() in ["exit", "quit"]:
            break

        docs = retriever.get_relevant_docs(query)
        prompt = prompt_builder.build(query, docs)
        answer = llm.ask(prompt)

        print(f"\n💬 챗봇 답변:\n{answer}\n")
