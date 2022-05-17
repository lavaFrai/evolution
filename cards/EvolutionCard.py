from classes.entity import *


class EvolutionCard:
    def __init__(self, name, description, weight=0):
        # Имя карты, используется для сравнения карт и выводится пользователю
        self.name = name
        # Описание, должно объяснять пользователю, как работает эта карта
        self.description = description
        # "Вес" карты - сколько она добавляет потребности в еде этому животному
        self.weight = weight

    # Событие вызывается, когда данное животное атаковано хищником
    # Возвращает true, если данная карта способна защитить животное от атакующего хищника
    def on_attacked(self,
                    defending: Entity,  # Защищающееся животное - то животное, которому принадлежит карта
                    predator: Entity    # Атакующее животное - хищник
                    ) -> bool:
        return False
