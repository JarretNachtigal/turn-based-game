import csv
from summon import Summon, Skill
from player import Player
from gameboard import GameBoard

MENU_DISPLAY = "\
    _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._ \n \
.-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.\n \
)                                                                             (\n \
(                                                                             )\n \
)                                                                             (\n \
(                                                                             )\n \
)                                                                             (\n \
(                                                                             )\n \
)                                                                             (\n \
(                        Welcome To the Fucking Game                          )\n \
)                                                                             (\n \
(                                                                             )\n \
)                                                                             (\n \
(                                                                             )\n \
)                                                                             (\n \
(___       _       _       _       _       _       _       _       _       ___)\n \
    `-._.-' (___ _) (__ _ ) (_   _) (__  _) ( __ _) (__  _) (__ _ ) `-._.-'\n \
            `-._.-' (  ___) ( _  _) ( _ __) (_  __) (__ __) `-._.-'\n \
                    `-._.-' (__  _) (__  _) (_ _ _) `-._.-'\n \
                            `-._.-' (_ ___) `-._.-'\n \
                                    `-._.-'"


def main():

    print(MENU_DISPLAY)

    # player data is filled before game loop begins
    # passed into game_loop as paramaters
    # characters = [] # will hold instantiated characters at the highest scope MAYBE?
    # character_abilities = [] # will hold instantiated character abilities at the highest scope MAYBE?
    players = read_players(1, 2)
    character_1, character_2 = read_summons(1, 2)
    players[1].character = character_1
    players[1].character = character_2
    # this setup method will get all the objects for the game ready MAYBE?
    # setup()
    # game loop call

    # begin GameBoardtest
    gameboard = GameBoard(players[0])
    game_loop(players)


# this method handles the player data and controlling turns and continues until the game is over
def game_loop(players):
    # overworld stuff? or maybe this game loop is only for combat sections

    # will continue combat until 0 is input to exit
    while (turn(players[0], players[1])):
        pass


# def display_battle_menu(turn, player_1, player_2):
#     if turn == 0:
#         player = player_1
#     else:
#         player = player_2

#     print("-----------------------------")
#     print("Please Select Your Spell, ", player.name)
#     for spell in player.active_summon["moveset"]:
#         name = spell["name"]
#         physical_damage = spell["physical_damage"]
#         magic_damage = spell["magic_damage"]
#         spell_pos = spell["pos"]
#         print(f"----- {spell_pos} -----")
#         print(f"----- {name} -----")
#         print(f"----- physical damage: {physical_damage} -----")
#         print(f"----- magic damage: {magic_damage} -----")
#         print("-----------------------------")
#         print("")
#         print("")

# this method is passed the players? characters? each turn (1 player goes, not both) and handles everything for each turn


def turn(player_1, player_2):
    # note: --print a nice command line prompt
    # note: --later implement a little vm to read a string describing an attack and its effects
    # this way attacks can be defined as data and be customized for anything
    # note: --add robust menu options for the player - including a display of their character's specific abilities as menu items
    # display_battle_menu(turn, player_1, player_2)
    print(f"{player_1.name}, Please Select a Combat Option:")
    # these printed fields can be replaced with data and a loop
    user_input = int(input())

    # figure out a better way to make these ability method calls
    # store functions in a dictionary? - seems troll
    match user_input:
        case 0:
            return 0
        case 1:
            basic_attack(player_1.character, player_2.character)
            return 1
        case 1:
            fireball(player_1.character, player_2.character)
            return 1
        case _:
            print("not recognized")
            return 1  # does not end execution


# ch1 deals his attack state to player 2
# this value is reduced by player 2's defense stat
# this needs to integrate an algorithm for damage reduction by def
def basic_attack(ch1: Summon, ch2: Summon):
    # for now this will deal 5 damage regardless of stats
    ch2.hp = ch2.hp - ch1.atk


# could be obsolete after a while
def fireball(ch1: Summon, ch2: Summon):
    ch2.hp = ch2.hp - 10

# this function reads playerdata.csv and returns data necessary for instantiating Player objects


def read_players(p1_id, p2_id):
    players = [0, 1]
    with open('playerdata.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == str(p1_id):
                players[0] = Player(row[0], row[1])
            elif row[0] == str(p2_id):
                players[1] = Player(row[0], row[1])
    # print(players)
    return players


# this function reads playerdata.csv and returns data necessary for instantiating Summon objects
def read_summons(ch1_id, ch2_id):
    summons = [1, 2]
    with open('characterdata.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == str(ch1_id):
                summons[0] = Summon(
                    row[0], row[1], row[2], row[3], row[4])
            elif row[0] == str(ch2_id):
                summons[1] = Summon(
                    row[0], row[1], row[2], row[3], row[4])
    # print(characters)
    return summons[0], summons[1]


# there must be a smarter way to do this
# this function reads characterabilitydata.csv and returns data necessary instantiating CharacterAbility objects
def read_character_ability(mv_id):
    summons = [1, 2]
    with open('characterabilitydata.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] == str(mv_id):
                summons[0] = Skill(
                    row[0], row[1], row[2], row[3], row[4])
            elif row[0] == str(mv_id):
                summons[1] = Summon(
                    row[0], row[1], row[2], row[3], row[4])
    print(summons)
    return summons[0], summons[1]


# if __name__ == "__main__":
#     main()
