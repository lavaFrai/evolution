from cards.EvolutionCard import *
from cards.SharpVision import *


class Camouflage(EvolutionCard):
    def __init__(self):
        super().__init__(name="Камуфляж",
                         description="🦎 может быть атаковано только хищником со свойством ОСТРОЕ ЗРЕНИЕ")

    def on_attacked(self, defending: Entity, predator: Entity) -> bool:
        for feature in predator.features:
            if feature.name == SharpVision().name:
                return False
        return True
