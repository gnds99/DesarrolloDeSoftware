from abc import ABC, abstractclassmethod, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw():
        pass