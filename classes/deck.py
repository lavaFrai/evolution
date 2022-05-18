import random

from cards.HighBodyWeight import *
from cards.Camouflage import *
from cards.SharpVision import *
from cards.TailLoose import *
from cards.Swimming import *

from classes.card import *
from classes.player import *


class EvolutionDeck:
    SAMPLE_DECK = [EvolutionCard(HighBodyWeight()) for i in range(8)] + \
                  [EvolutionCard(Camouflage()) for i in range(4)] + \
                  [EvolutionCard(SharpVision()) for i in range(4)] + \
                  [EvolutionCard(TailLoose()) for i in range(4)] + \
                  [EvolutionCard(Swimming()) for i in range(8)]

    def __init__(self, cards: list):
        self.cards = cards

    def Shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, key) -> EvolutionCard:
        return self.cards[key]

    def __len__(self) -> int:
        return len(self.cards)

    def GiveNextCard(self, player: EvolutionPlayer):
        player.GiveCard(self.cards.pop(0))
