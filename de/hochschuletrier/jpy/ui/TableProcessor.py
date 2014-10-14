__author__ = 'miko'
from de.hochschuletrier.jpy.ui.JPYLabel import JPYLabel
from de.hochschuletrier.jpy.ui.JPYUserLabel import JPYUserLabel
from de.hochschuletrier.jpy.ui.JPYButton import JPYButton
from de.hochschuletrier.jpy.jason.JSONHandler import JSONHandler


class TableProcessor:
    cols = 6
    rows = 6
    def __init__(self, parent, root, questionset):
        self.root = root
        self.parent = parent
        self.buildTableHead()
        self.buildTableBody()
        self.buildCandidates()

    def buildTableHead(self):
        for header in range(6):
            JPYLabel(self.parent, text=self.root.questionManager.categories[header]).grid(row=0, column=header)

    def buildTableBody(self):
        for row in range(1, 6):
            for col in range(6):
                values = [100, 200, 300, 400, 500, 600]
                if self.root.questionManager.questionSet[col][row - 1] == 1:
                    text = "$"+str(values[row])
                else:
                    text = ""
                JPYButton(
                    self.parent,
                    question=self.root.questionManager.questions[self.root.questionManager.categories[col]][row-1],
                    text=text,
                    worth=values[row],
                    questionID=[col, row - 1],
                    borderwidth=1,
                ).grid(row=row, column=col)

    def buildCandidates(self):
        colors = ["red", "green", "purple", "brown", "black", "yellow"]
        col = 0
        max = len(self.root.candidateManager.candidates)
        span = int(round(6 / max))

        for candidate in self.root.candidateManager.candidates:
            cLabel = JPYUserLabel(self.parent, back=colors[candidate.id], user=candidate)
            cLabel.grid(row=6, column=col, columnspan=span)
            col += span

        if span == 1:
            for empty in range(6 - len(self.root.candidateManager.candidates)):
                JPYLabel(self.parent, background="black", text="").grid(row=6, column=len(self.root.candidateManager.candidates)+ empty)