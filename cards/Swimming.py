from cards.EvolutionFeature import *


class Swimming(EvolutionFeature):
    def __init__(self):
        super().__init__(name="Водоплавающее",
                         description="🦎 может быть атаковано только хищником со свойством ВОДОПЛАВАЮЩЕЕ. "
                                     "Хищник со свойством ВОДОПЛАВАЮЩЕЕ не может атаковать 🦎 без свойства ВОДОПЛАВАЮЩЕЕ.")

    def on_attacked(self, defending: Entity, predator: Entity) -> bool:
        for feature in predator.features:
            if feature.name == self.name:
                return False
        return True

    def on_attack(self, predator: Entity, target: Entity) -> bool:
        for feature in target.features:
            if feature.name == self.name:
                return False
        return True
