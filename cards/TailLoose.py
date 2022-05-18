from cards.EvolutionFeature import *


class TailLoose(EvolutionFeature):
    def __init__(self):
        super().__init__(name="Отбрасывание хвоста",
                         description="ОТБРАСЫВАНИЕ ХВОСТА. Когда атаковано хищником, поместить в сброс карту этого "
                                     "или другого имеющегося у свойства - остается в живых. Хищник получает только одну.")

    def on_attacked(self, defending: Entity, predator: Entity) -> bool:
        predator.AddFish(1)
        defending.RemoveFeature(self)
        return True
