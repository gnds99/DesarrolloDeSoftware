from ChatRoom import *

class User:

    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def sendMessage(self, message):
        ChatRoom.showMessage(self, message)
