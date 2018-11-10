print("Welcome to the Dice-Rolling Simulator")

turns = 0

name = raw_input("What is your name, Player 1?")

name_2 = raw_input("What is your name, Player 2?")

print("Hello, " + name + ", and " + name_2 +"!")

import random

roll_1 = random.randint(1, 20)

roll_2 = random.randint(1, 20)

roll_3 = random.randint(1, 20)

player_1_sum = roll_1 + roll_2 + roll_3

roll_4 = random.randint(1, 20)

roll_5 = random.randint(1, 20)

roll_6 = random.randint(1, 20)

player_2_sum = roll_4 + roll_5 + roll_6

while turns < 1:
    raw_input("Press any key to roll, Player 1")

    print("Player 1, you rolled:" + " " + str(roll_1) + ", " + str(roll_2) + ", and " + str(roll_3))

    print("Player 1, your total score is " + str(player_1_sum))

    turns = turns + 2

raw_input("Click to start Player 2!")

while turns > 1 and turns < 4:
    raw_input("Press any key to roll, Player 2")

    print("Player 2, you rolled:" + " " + str(roll_4) + ", " + str(roll_5) + ", and " + str(roll_6))

    print("Player 2, your total score is " + str(player_2_sum))

    turns = turns + 2

if str(player_1_sum) > str(player_2_sum):
    print(name + " wins!")
elif str(player_1_sum) < str(player_2_sum):
    print(name_2 + " wins!")
elif str(player_1_sum) == str(player_2_sum):
    print("It's a tie!")







