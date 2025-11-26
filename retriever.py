class Retriever:
    def __init__(self):
        # 실제 VectorDB 연동 전까지는 임시 문서
        self.docs = {
            "고혈압": "고혈압 환자는 나트륨을 줄이고 칼륨이 많은 식품을 섭취해야 합니다.",
            "당뇨": "당뇨 환자는 GI 지수가 낮고 섬유질이 풍부한 음식을 섭취하는 것이 좋습니다.",
        }

    def get_relevant_docs(self, query):
        relevant = []
        for keyword, doc in self.docs.items():
            if keyword in query:
                relevant.append(doc)
        return relevant
