class Category:
    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location
        self.questions = []
        self.answers = []

    def addQuestion(self, question, answer):
        self.questions.append(str(question))
        self.answers.append(str(answer))