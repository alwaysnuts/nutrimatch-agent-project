class ChatHistory:
    def __init__(self):
        self.history = []

    def add(self, user_input, bot_output):
        self.history.append((user_input, bot_output))
        if len(self.history) > 5:
            self.history.pop(0)

    def get_context(self):
        return "\n".join([f"Q: {q}\nA: {a}" for q, a in self.history])
