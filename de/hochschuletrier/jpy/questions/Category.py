class Category:
    def __init__(self, type, location):
        self.type = type
        self.location = location
        self.questions = []
        self.answers = []

    def addQuestion(self, question, answer):
        self.questions.append(str(question))
        self.questions.append(str(answer))