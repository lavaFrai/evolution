from cards.HighBodyWeight import *
from cards.Camouflage import *
from cards.SharpVision import *

from classes.entity import *


animal1 = Entity()
animal2 = Entity()

animal1.AddFeature(HighBodyWeight())
animal2.AddFeature(HighBodyWeight())

animal1.AddFeature(Camouflage())
animal2.AddFeature(SharpVision())

print(animal2.Attack(animal1))
