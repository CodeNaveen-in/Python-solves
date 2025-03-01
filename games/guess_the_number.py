import random

#Getting basics from the user
print ('''Welcome to the NUMBER GUESSING GAME..
       Aim : 
       1. To find out what the number computer has guessed.
       2. There are two modes of the game play wisely!
       3. Use positive numbers only''')
name = input("\nHello User please give us your name.. : ")

lb=int(input(f"Hello {name}, Select the minimum range for number: "))
ub=int(input(f"Hello {name}, Please enter the upper bound range of the game : "))
mode = input("Enter your preffered game mode (Easy/Hard) : ")

#Making our number and user choice
num = random.randint(lb,ub)
count = 1
choice = int(input("Choose your Number : "))
if (choice >=num+5):
    print ("Your choice was way too high.")
elif (choice <= num-5):
    print ("Your choice was way too low.")
elif (abs(num-choice)<=5):
    print ("You are close keep going!!!")

if (mode.lower() =="easy"):
    #Iterating the count and comparing choice in easy mode
    while choice != num :
        choice = int(input(" \nWrong! try again : "))
        if (choice >=num+5):
            print ("Your choice was way too high.")
        elif (choice <= num-5):
            print ("Your choice was way too low.")
        elif (abs(num-choice)<=5):
            print ("You are close keep going!!!")
        count +=1
    #Result when things are right
    print (f"You guessed it {name}, it was {num} and had the count of {count}")

elif (mode.lower() == "hard"):
    #Iterating and counting in hard mode
    while (choice != num) and (count<=7):
        choice = int(input(" \nWrong! try again : "))
        if (choice >=num+5):
            print (f"Your choice was way too high. {7-count} chances are left")
        elif (choice <= num-5):
            print (f"Your choice was way too low. {7-count} chances are left")
        elif (abs(num-choice)<=5):
            print (f"You are close keep going!!! {7-count} chances are left")
        count +=1
    
    #Result when things are right
    if (choice == num):
        print (f"\nYou guessed it {name}, it was {num} and had the count of {count}")
    else :
        print (f"\nSorry you lose!!! {name} You could not guess the number in {count} moves, it was {num}")