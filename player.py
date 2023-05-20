# this class represents a human or AI player - not a character in game
# if the game takes a more PvE route, human and AI players will need to be abstracted somehow
class Player:

    def __init__(self, player_id, player_name) -> None:
        self.id = player_id
        self.player_name = player_name