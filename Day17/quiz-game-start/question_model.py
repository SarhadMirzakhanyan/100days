class Question():
    def __init__(self,question,answer) -> None:
        self.question = question
        self.answer = answer
    def __repr__(self) -> str:
        return f"{self.question}: {self.answer}"