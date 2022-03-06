from EnemyDecorator import *

class ArmourDecorator(EnemyDecorator):

    def __init__(self, enemy):
        super().__init__(enemy)
    
    def takeDamage(self):
        return super().takeDamage() / 1.5
    