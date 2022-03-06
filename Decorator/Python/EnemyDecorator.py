
from Enemy import *
class EnemyDecorator(Enemy):

    def __init__(self, enemy):
        self.enemy = enemy
    
    def takeDamage(self):
        return self.enemy.takeDamage()
    
