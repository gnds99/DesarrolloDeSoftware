from EnemyDecorator import *
class HelmetDecorator(EnemyDecorator):
    
    def __init__(self, enemy):
        super().__init__(enemy)

    def takeDamage(self):
        return super().takeDamage() / 2
        #return self.enemy.takeDamage() / 2