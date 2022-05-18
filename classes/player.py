from classes.card import *
from classes.entity import *


class EvolutionPlayer:
    def __init__(self):
        self.cards: list = list()
        self.animals: list = list()

    def GiveCard(self, card: EvolutionCard):
        self.cards.append(card)

    def CreateAnimalFromCard(self, card_id):
        self.animals.append(Entity(self.cards.pop(card_id)))

    def PrintAnimal(self, player_animal_index):
        print(f"{player_animal_index}:")
        for player_animal_feature_index in range(len(self.animals[player_animal_index].features)):
            print('┣' if player_animal_feature_index != len(self.animals[player_animal_index].features) - 1
                  else '┗',
                  self.animals[player_animal_index].features[player_animal_feature_index].name)

    def PrintAnimals(self):
        for i in range(len(self.animals)):
            self.PrintAnimal(i)

