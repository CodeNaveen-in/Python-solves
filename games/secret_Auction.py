logo = '''
  ____                 _            _   _             
 / ___|___  _ __  ___ | |_ ___  ___| |_| |_ ___ _ __  
| |   / _ \| '_ \/ __|| __/ _ \/ __| __| __/ _ \ '__| 
| |__| (_) | | | \__ \| ||  __/\__ \ |_| ||  __/ |    
 \____\___/|_| |_|___/ \__\___||___/\__|\__\___|_|    

      >>> Secret Auction Program <<<'''

print(logo)
print("\n\n Give secret bids and win the auction with highest bid!!!")

player_data ={}
gameover = False

while (not gameover):
    name = input("Hello dear player, enter your name:\t")
    if name in player_data:
        name += "_1"
    player_data[name] = float(input(f"Hey {name}, Enter your bid amount :\t$"))
    choice = input("You wanna play? Yes or No\t").lower()
    print("\n" * 100)
    
    if (choice == "no"):
        gameover = True
        print("Thank you for playing.. !!!")
        highest_bid = max(player_data.items(), key=lambda item: item[1])
        print(f"Winning bid is {highest_bid[1]} by {highest_bid[0]}")
        print(player_data)

choice= input("You want top 3 bids? yes or no\t")
if (choice == "yes"):
    sorted_list= sorted(player_data.items(), key=lambda item:item[1] )
    for rank, (name, bid) in enumerate(sorted_list[:3], start = 1):
        print(f"{rank}. {name} with the bid of ${bid}")
if (choice == "no"):
    print(f"OK but the sorted list you could have asked")