#Greet user
print("Hello Dear User... WELCOME to PIZZERIA !")

#Ask for pizza size
bill = 0
pizza_size = input("What size of pizza you want?? s, m or b : ")
if (pizza_size == "s"):
    bill += 15
elif (pizza_size == "m"):
    bill +=20
elif (pizza_size == "b"):
    bill +=30
else:
    print("NOT a correct response!!!")

#Ask for peperroni and adjust pricing
pepperoni = input("You want pepperoni on your pizza? y or n: ")
if (pepperoni == "y"):
    if (pizza_size == "s"):
        bill += 2
    else:
        bill += 3

#Ask for extra cheese and adjsut pricing
extra_cheese = input(" Would extra cheese make your day? y or n : ")
if (extra_cheese == "y"):
    bill += 2

print(f"Thank you for setting up your pizza! \n Your bill turns out to be {bill} \n With your pizza size as {pizza_size} and preference for pepperoni as {pepperoni} and cheese as {extra_cheese}")