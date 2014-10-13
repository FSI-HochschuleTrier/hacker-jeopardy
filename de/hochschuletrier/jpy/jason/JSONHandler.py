__author__ = 'miko'

import json
from collections import OrderedDict

class JSONHandler:
    filepath = ""
    def __init__(self, file):
        self.categories = []
        self.file = file
        self.questions = dict()
        with open(JSONHandler.filepath + self.file) as data_file:
            jsondata = json.load(data_file, object_pairs_hook=OrderedDict)

        for category in jsondata:
            self.categories.append(str(category.encode("utf-8")))
            self.questions[category] = []
            for question in jsondata[category]:
                self.questions[category].append(str(question.encode("utf-8")))

    def getCategories(self):
        return self.categories

    def getQuestions(self):
        return self.questions