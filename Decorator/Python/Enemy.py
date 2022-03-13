from abc import ABC, abstractmethod
class Enemy(ABC):
    @abstractmethod
    def takeDamage(self):
        pass