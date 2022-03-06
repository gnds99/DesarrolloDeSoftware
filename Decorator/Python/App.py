from BaseEnemy import *
from HelmetDecorator import *
from ArmourDecorator import *
from DifficultEnemy import *

#enemy = BaseEnemy() # descomentar enemy = BaseEnemy() para probar el reciclado de las clases decoradoras
enemy = DifficultEnemy() # si descomenta la anterior, comentar esta linea
enemyWithHelmet = HelmetDecorator(enemy)
enemyWithHelmetAndArmour = ArmourDecorator(enemyWithHelmet)
computedDamage = enemyWithHelmetAndArmour.takeDamage()
print(computedDamage)