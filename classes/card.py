from cards.EvolutionFeature import *
from classes.entity import *


class EvolutionCard:
    def __init__(self, first_side: EvolutionFeature, second_side: EvolutionFeature = None):
        self.first_side = first_side
        self.second_side = second_side

    def Cast(self, animal: Entity, side=1):
        if side not in range(1, 3): raise Exception("Invalid card side")
        if side == 1:
            if self.first_side.auto_cast:
                self.first_side.on_cast(animal, type(self.first_side))
            else:
                self.first_side.on_cast(animal)
        elif side == 2:
            if self.second_side.auto_cast:
                self.second_side.on_cast(animal, type(self.second_side))
            else:
                self.second_side.on_cast(animal)

    def __str__(self):
        return self.first_side.name if self.second_side is None else self.first_side.name + ':' + self.second_side.name
