class Caretaker:
    def __init__(self):
        self._mementos = []
    
    def addMemento(self, m):
        self._mementos.append(m)
    
    def getMemento(self, index):
        return self._mementos[index]


