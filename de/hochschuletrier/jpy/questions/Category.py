class Category:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.questions = []
		self.answers = []

	def addQuestion(self, question, answer):
		self.questions.append(question.encode("utf-8"))
		self.answers.append(answer.encode("utf-8"))
