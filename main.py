import os

import pyautogui as pyautogui

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

# Да, знаю, говнокод, потом все переделать надо будет, но это просто для дебага

while True:
    last_i = 0
    i = 0
    while i < len(game.players):
        # if i != last_i:
        #     os.system('cls')
        last_i = i
        passed = 0
        action = input(f"Player{i} > ").split()

        if action[0] == "cards":
            for card_index in range(len(game.players[i].cards)):
                print(f"{card_index}.", game.players[i].cards[card_index])

        elif action[0] == "animals":
            game.players[i].PrintAnimals()

        elif action[0] == "description":
            print(game.players[i].cards[int(action[1])].first_side.description)

        elif action[0] == "new":
            game.players[i].CreateAnimalFromCard(int(action[1]))

            i += 1
        elif action[0] == "add":
            game.players[i].animals[int(action[2])].AddFeature(
                game.players[i].cards[int(action[1])].first_side
            )
            i += 1
        # Next handlers

        elif action[0] == "pass":
            passed += 1
            i += 1
            pass
        elif action[0] == "help":
            print("cards - посмотреть ваши карты\n"
                  "animals - вывести всех ваших животных\n"
                  "pass - пропустить ход\n"
                  "description <card_number> - описание одной из ваших карт\n"
                  "new <card_number> - создать животное из карты\n"
                  "add <card_number> <animal_number> - добавляет карту к животному\n"
                  "Когда все игроки пропустят ход, начнется следующая фаза игры")
        else:
            print(f"Unexpected command: {action[0]}")
    if passed == len(game.players):
        print("Next game phase")
