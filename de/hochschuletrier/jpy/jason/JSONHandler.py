from de.hochschuletrier.jpy.questions.Category import Category

__author__ = 'miko'

import json
from collections import OrderedDict


class JSONHandler:
    filepath = ""

    def __init__(self, file):
        self.categories = []
        self.file = file
        with open(JSONHandler.filepath + self.file) as data_file:
            jsondata = json.load(data_file, object_pairs_hook=OrderedDict)

        self.double = jsondata["double"]
        print("double: " + str(self.double))

        cats = jsondata["categories"]
        for cat in cats:
            tempcat = Category(cat["name"], cat["type"], cat["location"])

            for i in range(len(cat["questions"])):
                q = cat["questions"][i]
                a = cat["answers"][i]
                #print(q + " -> " + a)
                tempcat.addQuestion(q, a)

            self.categories.append(tempcat)

    def getCategories(self):
        return self.categories

    def getQuestions(self):
        return self.questions