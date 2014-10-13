__author__ = 'miko'


class JPYLogger:
    def __init__(self, caller):
        self.caller = caller.__class__.__name__

    def log(self, message):
        print self.__class__.__name__ + "[LOG] >> " + self.caller + "\t--  " + message

    def prompt(self, message):
        print self.__class__.__name__ + "[GAMEINFO] >> " + self.caller + "\t--  " + message