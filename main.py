import csv


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

# this class represents a human or AI player - not a character in game
class Player:

    def __init__(self, player_id, player_name) -> None:
        self.id = player_id
        self.player_name = player_name


def main():

    # player data is filled before game loop begins
    # passed into game_loop as paramaters
    
    player_1, player_2 = read_players(1, 2)
    character_1, character_2 = read_characters(1, 2)
    player_1.character = character_1
    player_2.character = character_2
    # this setup method will get all the objects for the game ready MAYBE?
    # setup()
    # game loop call
    game_loop(player_1, player_2)


# this method handles the player data and controlling turns and continues until the game is over
def game_loop(player_1, player_2):
    # while not game_end:
    #     turn(player_1, player_2)
    #     if player_1.character.hp <= 0 or player_2.character.hp <= 0:
    #         game_end = True
    #     turn(player_2, player_1)
    #     print(player_1.character.hp, " ", player_2.character.hp)
    #     if player_1.character.hp <= 0 or player_2.character.hp <= 0:
    #         game_end = True
    while(turn(player_1, player_2)):
        pass

    

# this method is passed the players? characters? each turn (1 player goes, not both) and handles everything for each turn
def turn(player_1, player_2):
    # note: --print a nice command line prompt
    # note: --later implement a little vm to read a string describing an attack and its effects
    # this way attacks can be defined as data and be customized for anything
    # note: --add robust menu options for the player
    print(f"{player_1.player_name}, Please Select a Combat Option:")
    print("0: end the game")
    print("1: basic attack")
    user_input = int(input())
    
    match user_input:
        case 0:
            return 0
        case 1:
            basic_attack(player_1.character, player_2.character)
            return 1
        case _:
            print("not recognized")
            # what happens if no return?
        

    


# ch1 deals his attack state to player 2
# this value is reduced by player 2's defense stat
# this needs to integrate an algorithm for damage reduction by def
def basic_attack(ch1: Character, ch2: Character):
    # for now this will deal 5 damage regardless of stats
    ch2.hp = ch2.hp - 10


# this function reads playerdata.csv and returns data necessary for instantiating Player objects
def read_players(p1_id,p2_id):
    players = [0,1]
    with open('playerdata.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == str(p1_id):
                players[0] = Player(row[0], row[1])
            elif row[0] == str(p2_id):
                players[1] = Player(row[0], row[1])
    print(players)
    return players[0], players[1]


# this function reads playerdata.csv and returns data necessary for instantiating Character objects
def read_characters(ch1_id, ch2_id):
    characters = [1,2]
    with open('characterdata.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == str(ch1_id):
                characters[0] = Character(row[0], row[1], row[2], row[3], row[4])
            elif row[0] == str(ch2_id):
                characters[1] = Character(row[0], row[1], row[2], row[3], row[4])
    print(characters)
    return characters[0], characters[1]

if __name__ == "__main__":
    main()