from cards.EvolutionFeature import *


class HighBodyWeight(EvolutionFeature):
    def __init__(self):
        super().__init__(name="Большой",
                         description="Данное 🦎 может быть атаковано только \"БОЛЬШИМ\" хищником",
                         weight=1)

    def on_attacked(self, defending: Entity, predator: Entity) -> bool:
        for feature in predator.features:
            if feature.name == self.name:
                return False
        return True
