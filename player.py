# this class represents a human or AI player - not a character in game
# if the game takes a more PvE route, human and AI players will need to be abstracted somehow
class Player:

    def __init__(self, p_id, name, summons=[], items=[], x_pos=0, y_pos=0):
        self.id = p_id
        self.name = name
        # data that will be accessed through a player
        self.summons = summons  # maybe refer to a Party class?
        self.items = items  # maybe refer to an Inventory class?
        self.active_summon = None
        self.x_pos = x_pos
        self.y_pos = y_pos


# this needs a way to keep track of whether it is the player or an antagonist
# might be another place for an interface instead of inheritence
