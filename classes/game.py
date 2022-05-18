from classes.deck import *


class EvolutionGame:
    PHASE_BUILDING = 1
    PHASE_EATING = 2
    PHASE_EXTINCTION = 3

    def __init__(self, players_count):
        if players_count not in range(2, 7):
            raise Exception("Invalid players count")
        self.phase = EvolutionGame.PHASE_BUILDING
        self.deck = EvolutionDeck(EvolutionDeck.SAMPLE_DECK)
        self.deck.Shuffle()
