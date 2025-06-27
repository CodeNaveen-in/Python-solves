import random
print("Hey Hey join in fot number guess.. \n-5 chance on hard and 10 on easy \n-Below or above 5 nums is deemed high")
low_num = int(input("Enter low range number :"))
high_num = int(input("Enter the high range number :")) + 1

num = random.randint(low_num, high_num)
mchoice = input("Which mode are we planning? easy or hard?").lower()
if (mchoice == "easy"):
    count = 10
elif (mchoice == "hard"):
    count = 5

chance = 0
while (chance < count):
    choice = int(input(" Game has started.. What's yoru choice? \t:"))
    if (abs(num-choice) < 5):
        if (num == choice):
            print(f"WOOHOOO.. You won the num was {num}")
            break
        else:
            print(f"You are nearby the number.. Don't go much far")
    else:
        if (num > choice):
            print(f"Your choice is too low {choice}")
        else:
            print(f"Your choice is too high")
    chance += 1