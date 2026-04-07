import random

opt = ["snake", "water", "gun"]

num = random.randint(1,3)
c_choice = opt[num-1]

inp = int(input("Enter your choice : \n1.Snake \n2.Water \n3.Gun \n\t: "))
h_choice = opt[inp-1]

def whowin( val1, val2):
    if (val1 == val2):
        return None
    elif (val1 == "snake" and val2 == "water") or (val1 == "water" and val2 == "gun") or (val1 == "gun" and val2 == "snake"):
        return val1
    else: 
        return val2
    
winner = whowin(c_choice, h_choice)

if (winner == None): # can also be done with if (winner is None) :
    print ("It was a draw ")
elif (winner == c_choice):
    print (f"Computer won by choosing {c_choice} and human chose {h_choice}")
else : 
    print (f"Human won by choosing {h_choice} and computer chose {c_choice}")