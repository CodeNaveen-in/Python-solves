print(r"""
   ____  ___   ___ _____   ___  _____   ___ ___ _____ _   _ _____ ____
  / ___|/ _ \ / _ \ ____| / _ \| ____| |  _ \_ _|_   _| | | | ____|  _ \
 | |   | | | | | | |  _| | | | |  _|   | |_) | |  | | | |_| |  _| | |_) |
 | |___| |_| | |_| | |___| |_| | |___   |  __/| |  | | |  _  | |___|  _ <
  \____|\___/ \___/|_____| \___/|_____| |_|  |___| |_| |_| |_|_____|_| \_\

                    ~ THE LOST CAVE ~
                 ========================
                    ENTER IF YOU DARE...
""")

print("You found yourself stranded in front of a cave.")
print("(1.) Go in")
print("(2.) Stay out")

choice = int(input("What is your choice? 1 or 2: "))

if choice == 1:
    print("\nYou enter the cave and walk for hours.")
    print("You find two paths.")
    print("(1.) Go Right")
    print("(2.) Go Left")

    choice = int(input("What is your choice? 1 or 2: "))

    if choice == 1:
        print("\nYou go right and find a river.")
        print("(1.) Swim across")
        print("(2.) Follow the river")

        choice = int(input("What is your choice? 1 or 2: "))

        if choice == 1:
            print("\nThe river is too deep!")
            print("You get swept away. Game Over!")

        elif choice == 2:
            print("\nYou follow the river and discover a hidden exit!")
            print("You escaped the cave. YOU WIN!")

        else:
            print("\nInvalid choice. Game Over!")

    elif choice == 2:
        print("\nYou go left and find a treasure chest.")
        print("(1.) Open the chest")
        print("(2.) Leave it alone")

        choice = int(input("What is your choice? 1 or 2: "))

        if choice == 1:
            print("\nThe chest contains gold and a map!")
            print("The map leads you safely out of the cave.")
            print("YOU WIN!")

        elif choice == 2:
            print("\nYou leave the treasure and continue walking.")
            print("You eventually find an exit.")
            print("You survived, but missed the treasure!")

        else:
            print("\nInvalid choice. Game Over!")

    else:
        print("\nYou stand there unable to decide.")
        print("You get lost in the cave. Game Over!")

elif choice == 2:
    print("\nYou decided to stay outside.")
    print("After hours of waiting, you find nothing to eat.")
    print("You starved. Game Over!")

else:
    print("\nThat was not a valid choice. Game Over!")
