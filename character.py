# this class represents an ingame character capable of battle
class Character:

    def __init__(self, id, name, hp, atk, defense):
        self.id = id
        self.name = name
        self.hp = int(hp)
        self.atk = int(atk)
        self.defense = int(defense)
        self.character = None

    # @property
    # def hp(self):
    #     return self.hp

    # @hp.setter
    # def hp(self, hp):
    #     self.hp = hp

# instances of this class represents a move that a character can learn and use
class CharacterAbility:

    def __init__(self, id, name, type, damage, cost) -> None:
        self.id = id
        self.name = name
        self.damage = damage
        self.cost = cost