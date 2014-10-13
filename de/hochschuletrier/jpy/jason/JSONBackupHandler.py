__author__ = 'miko'
from json import *
import json
from de.hochschuletrier.jpy.candidates.Candidate import Candidate, SerializableCandidate

class JSONBackupHandler:
    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, 'w') as outfile:
            json.dump(data, outfile, default=SerializableCandidate.default)

    def load(self):
        with open(self.file) as data_file:
            jsondata = json.load(data_file)
        return jsondata
