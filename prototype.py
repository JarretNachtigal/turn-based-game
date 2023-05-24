import random

player_x = 0
player_y = 0
player_xp = 0

enemy_x = 0
enemy_y = 0

world_map = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
]

while (True):
    direction = input(f"player is at {player_x}, {player_y} ")
    print(f"enemy is at {enemy_x}, {enemy_y}")

    if direction == "w":
        player_y += 1
    elif direction == "a":
        player_x -= 1
    elif direction == "s":
        player_y -= 1
    elif direction == "d":
        player_x += 1

    enemy_move_input = random.randint(0, 3)
    movement_dict = {0: "w", 1: "a", 2: "s", 3: "d"}
    enemy_movement = movement_dict[enemy_move_input]

    # enemy move here

    if player_x == enemy_x and player_y == enemy_y:

        priority_queue = ["p1", "e"]
        player_attack = 10
        player_defense = 10
        player_hp = 50
        player_prio = 10
        enemy_attack = 5
        enemy_defense = 5
        enemy_hp = 20
        enemy_prio = 5
        while enemy_hp >= 0 and player_hp >= 0:
            print(f"priority: {priority_queue}")
            print(f"player_prio: {player_prio}")
            print(f"enemy_prio: {enemy_prio}")
            print("0: quit")
            print("1: attack")
            player_input = int(input("what will you do ?: \n"))
            if player_input == 0:
                break
            elif player_input == 1:
                if priority_queue[0] == "p1" and player_prio <= 0:
                    enemy_hp -= player_attack
                    player_prio = 50
                elif priority_queue[1] == "e" and enemy_prio <= 0:
                    player_hp -= enemy_attack
                    enemy_prio = 50

                player_prio -= 5
                enemy_prio -= 5

                if priority_queue[0] <= "p1" and player_prio >= enemy_prio and player_prio <= 0:
                    priority_queue = ["p1", "e"]
                elif priority_queue[0] <= "e" and enemy_prio <= 0:
                    priority_queue = ["e", "p1"]

        if player_hp <= 0:
            print("game over")
            break
        elif enemy_hp <= 0:
            xp_gained = 5
            print("you win")
            player_xp += 5
        else:
            print("game quit")
