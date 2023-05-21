# try not to use inheritence
# this represents the 'global' game state and contains the data for the Player, Summons, etc
class GameBoard:

    def __init__(self, player, entities=[]) -> None:
        # hold the actual player details
        self.player = player
        # this holds all entities relevent to the scene in an array
        self.entities = entities
