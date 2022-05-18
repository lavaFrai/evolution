class EvolutionPlayer:
    def __init__(self, players_count):
        if players_count not in range(2, 7):
            raise Exception("Invalid players count")
        self.cards: list = list()
