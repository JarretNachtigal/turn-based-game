class GameBoard:
    def placeholder():
        pass


# this represents the state of the game during combat
class CombatBoard:
    def __init__(self) -> None:
        self.player_turn = ""  # points to summons highest in prio queue? maybe rework?
        self.location = ""
        self.player_summon = ""
        self.gameQueue = GameQueue()


# this represents the game state out of combat
class OverWorld:
    def __init__(self) -> None:
        self.location = ""
        self.player = ""


# this object will be used on combat to keep track of the turn order in combat
# if tied, the player will go first (PvE)
class GameQueue:

    def __init__(self) -> None:
        self.priority = []

    def pop(self):
        self.priority.pop()

    def add(self, action):
        for i, action in enumerate(self.priority):
            print(i, action)
