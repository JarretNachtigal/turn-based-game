from sortedcontainers import SortedList

# try not to use inheritence
# this represents the 'global' game state and contains the data for the Player, Summons, etc


class GameBoard:

    def __init__(self, player, entities=[]) -> None:
        # hold the actual player details
        self.player = player
        # this holds all entities relevent to the scene in an array
        self.entities = entities
        self.summon = None
        # this should init dynamically to the first Person to have a turn
        self.active_player = None

        # the priority queue will sort by a Summon's speed/priority (left to right low to high)
        self.priority_queue = []

    # return the player who's turn it currently is
    @property
    def active_player(self):
        return self.active_player

    # this must always be sorted left to right low to high
    @property
    def priority_queue(self):
        pass

    # this must always be sorted left to right low to high
    @priority_queue.setter
    def priority_queue(self):
        pass

    # this method will set the next player through the active_player field and the next player in the list

    def set_next_player():
        pass

        # The gameboard will be used as a parent class or interface for the different screens of the game
        # this first one will be implemented as the combat screen, but likely it will be refactored into an interface that other
        # GameBoards will use.
        # it orchistrates the turns between players
        # it displays menus for the player and recieves their input
