# this class represents a human or AI player - not a character in game
# if the game takes a more PvE route, human and AI players will need to be abstracted somehow
class Player:

    def __init__(self, p_id, name, summons=[], items=[]):
        self.id = p_id
        self.name = name
        # data that will be accessed through a player
        self.summons = summons  # maybe refer to a Party class?
        self.items = items  # maybe refer to an Inventory class?
        self.active_summon = None