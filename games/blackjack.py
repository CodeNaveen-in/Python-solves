#TODO 1. Set the points/card values.
#TODO 2. Make functions for sum, for continuation.
#TODO 3. Ask and set player names and card
#TODO 4. Ask them for more cards? If yes add if not skip them over
#TODO 5. if any player bust they are out and stand so are they locked in

import random
card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {}

def addcard(name):
    card = random.choice(card_list)
    players[name].append(card)

def set_card(name):
    players[name] = []
    addcard(name)
    addcard(name)

def add_player():
    name=input("\nWelcome Player enter your name: \t")
    set_card(name)
    print(players[name])
    choice = input("Are there more players entering? y or n : ").lower()
    if (choice == "y"):
        add_player()
    else:
        set_card("Dealer")

def no_dealer_show():
    print("\n")
    for player, hand in players.items():
        if (player == "Dealer"):
            print(f"{player} : Hand is {hand[0]} and Secret")
        else:
            print(f"{player} : Hand is {hand}")

def cardSum(player):
    score = 0
    score_list = players[player]
    for i in score_list:
        score += i
    return score

def playTurn(player):
    score = cardSum(player)
    choice = input(f"\nDo you want to add a card {player}? y or n\t:")
    if (choice == 'y'):
        addcard(player)
        score = cardSum(player)
        print (f"Your deck is {players[player]} and score is {score}")
        if (score > 21):
            return score
        return playTurn(player)
    elif (choice =="n"):
        return score

""" GOOD REVIEW.. (as it shows updated score, returns on no, asks only if score less than 21 [better than my stack builder])
def playTurn(player):
    while True:
        score = cardSum(player)
        print(f"{player}'s hand: {players[player]} | Score: {score}")
        if score >= 21:
            return score
        choice = input(f"Do you want to add a card {player}? y or n\t:").strip().lower()
        if choice == "y":
            addcard(player)
        elif choice in ["n", ""]:
            return score"""
        
print("\nWelcome to the game of BLACKJACK..")
print("Rules are \n1. You get 2 cards at first \n2. You can choose to have more cards or not \n3. The goal is to get closest to 21 without going over.")

add_player()

active_p = list(players.keys())
for player in active_p:
    score = playTurn(player)    
    if (player == "Dealer"):
        while cardSum(player) < 17:
            addcard(player)
    else:
        if (score == 21):
            print(f"Wooho.. You've WON this BLACKJACK GAME {player} with a blackjack {score}.")
        elif (score > 21):
            print(f"Player {player} has gone busted")
    active_p.remove(player)
    print(f"The Score of {player} is {score}")
    no_dealer_show()
print(players)