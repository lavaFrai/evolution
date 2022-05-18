from classes.entity import *


class EvolutionFeature:
    def __init__(self, name, description, weight=0, auto_cast=True):
        # Имя карты, используется для сравнения карт и выводится пользователю
        self.name: str = name
        # Описание, должно объяснять пользователю, как работает эта карта
        self.description: str = description
        # "Вес" карты - сколько она добавляет потребности в еде этому животному
        self.weight: int = weight
        self.auto_cast: bool = auto_cast

    # Событие вызывается, когда данное животное атаковано хищником
    # Возвращает true, если данная карта способна защитить животное от атакующего хищника
    def on_attacked(self,
                    defending: Entity,  # Защищающееся животное - то животное, которому принадлежит карта
                    predator: Entity    # Атакующее животное - хищник
                    ) -> bool:
        return False

    # Событие вызывается, когда данное животное атакует другое
    # Возвращает true, если данная карта не мешает атаке и false, если мешает (Например, как водоплавающее, атакующее обычное)
    def on_attack(self,
                  predator: Entity,     # Атакующее животное - то животное, которому принадлежит карта
                  target: Entity        # Защищающееся животное - цель
                  ) -> bool:
        return False

    # Событие вызывается, когда свойство применяется к животному. По умолчанию, должно добавлять в features животного
    # экземпляр своего класса. Универсальная заглушка: def on_cast(self, animal: Entity): animal.AddFeature(type(self)())
    def on_cast(self,
                animal: Entity,         # Животное, к которому применяется карта
                auto_cast_class=None    # Если для этого экземпляра auto_cast = True, то в features животного экземпляр
                                        # будет этого класса будет добавлен автоматически
                ) -> None:
        if self.auto_cast and auto_cast_class is not None:
            animal.AddFeature(auto_cast_class())
        else:
            raise Exception("Cart casting ignored")
