from classes.deck import *
from classes.player import *


class EvolutionGame:
    PHASE_BUILDING = 1
    PHASE_EATING = 2
    PHASE_EXTINCTION = 3

    def __init__(self, players_count, cards_per_player=6, deck=EvolutionDeck.SAMPLE_DECK):
        self.deck = EvolutionDeck(deck)
        if players_count not in range(2, min(7, len(self.deck) // cards_per_player + 1)):
            raise Exception("Invalid players count")
        self.phase = EvolutionGame.PHASE_BUILDING
        self.deck.Shuffle()
        self.cards_per_player = cards_per_player
        self.players = [EvolutionPlayer() for _ in range(players_count)]
        for player in self.players:
            for i in range(cards_per_player):
                self.deck.GiveNextCard(player)
