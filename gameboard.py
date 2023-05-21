# try not to use inheritence
# this represents the 'global' game state and contains the data for the Player, Summons, etc
class GameBoard:

    def __init__(self, players=[]) -> None:
        self.players = players
