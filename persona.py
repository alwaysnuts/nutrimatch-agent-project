class Persona:
    def __init__(self, role="영양사"):
        self.role = role

    def get_system_prompt(self):
        if self.role == "영양사":
            return "당신은 따뜻하고 전문적인 영양사입니다. 식품과 질병에 대해 친절히 안내하세요."
        elif self.role == "의사":
            return "당신은 냉철하고 전문적인 내과의사입니다. 데이터 기반으로만 답변하세요."
        else:
            return "당신은 지식 기반 상담자입니다. 사용자 질문에 정확히 답하세요."
