from cards.HighBodyWeight import *
from cards.Camouflage import *
from cards.SharpVision import *
from cards.Swimming import *

from classes.entity import *


animal1 = Entity()
animal2 = Entity()

animal1.AddFeature(HighBodyWeight())
animal2.AddFeature(HighBodyWeight())

animal1.AddFeature(Camouflage())
animal2.AddFeature(SharpVision())

animal1.AddFeature(Swimming())
animal2.AddFeature(Swimming())

print("animal1:", animal1, sep='\n')
print("animal2:", animal2, sep='\n')

print("Animal2 attacking animal1:")
attack_result = animal2.Attack(animal1)
print("Success" if attack_result == 0 else "Not success")
