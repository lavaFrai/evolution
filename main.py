from cards.HighBodyWeight import *
from cards.Camouflage import *
from cards.SharpVision import *
from cards.TailLoose import *
from cards.Swimming import *

from classes.entity import *
from classes.game import *
from classes.card import *
from classes.player import *

game = EvolutionGame(2)
CamouflageCard = EvolutionCard(Camouflage())
HighBodyWeightCard = EvolutionCard(HighBodyWeight())
SharpVisionCard = EvolutionCard(SharpVision())
SwimmingCard = EvolutionCard(Swimming())
TailLooseCard = EvolutionCard(TailLoose())

animal1 = Entity()
animal2 = Entity()

HighBodyWeightCard.Cast(animal1)
HighBodyWeightCard.Cast(animal2)

CamouflageCard.Cast(animal1)
SharpVisionCard.Cast(animal2)

SwimmingCard.Cast(animal1)
SwimmingCard.Cast(animal2)

TailLooseCard.Cast(animal1)

# print("animal1:", animal1, sep='\n')
# print("animal2:", animal2, sep='\n')

print("Animal2 attacking animal1:")
attack_result = animal2.Attack(animal1)
print("Success\n" if attack_result == 0 else "Not success\n")

print("Animal2 attacking animal1:")
attack_result = animal2.Attack(animal1)
print("Success" if attack_result == 0 else "Not success")
