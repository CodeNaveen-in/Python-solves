#add modules
import random

#greet the user
print(r"""
     ✊ ROCK
     🖐 PAPER
     ✌ SCISSORS

   Let the battle begin!
    ➤ Python Edition 🐍
""")
print("\nHello USER, welcome to the ROCK, PAPER, SCISSOR game")

#get options
option = ["Rock", "Paper", "Scissors"]

#Set values and compare
player_choice = int(input("What do you choose? \nEnter the num 0:Rock, 1:Paper, 2:Scissor : \t"))
computer_choice = random.randint(0,2)

if (computer_choice == player_choice):
    print(f"\nWhoops, it's a DRAW as you chose {option[player_choice]} and computer chose {option[computer_choice]}")
elif (computer_choice != 2 and computer_choice < player_choice):
    print(f"\nYOU WON with the choice of {option[player_choice]} as the computer chose {option[computer_choice]}")
elif (computer_choice == 2 and player_choice == 0):
    print(f"\nYOU WON with the choice of {option[player_choice]} as the computer chose {option[computer_choice]}")
else:
    print(f"\nYOU LOST with computer choice of {option[computer_choice]} as the you chose {option[player_choice]}")
#Print the result