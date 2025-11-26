import os
import openai

class LLM:
    def __init__(self, model="gpt-3.5-turbo"):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model

    def ask(self, prompt):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "당신은 전문 영양사입니다. 논리적으로, 안전하게 답변하세요."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
