import random

ai_domains = {
    "Healthcare AI": ["diagnosis", "scan", "patient", "disease", "treatment"],
    "Agriculture AI": ["tractor", "drone", "weather", "crop", "soil"],
    "Finance AI": ["stock", "fraud", "loan", "data", "risk"],
    "Retail AI": ["customer", "shopping", "recommend", "inventory", "price"],
    "Education AI": ["learning", "quiz", "student", "teacher", "tutor"],
    "Transportation AI": ["traffic", "map", "car", "route", "driver"],
    "Smart Home AI": ["light", "voice", "alarm", "sensor", "device"]
}

''' #It has no use except for that one line below LOL but oh well conceptually it's good
key_len = len(ai_domains)
item_len = 0 
for key, value in ai_domains.items():
    print(key , "and", value , "and" , len(value))
    if (len(value) > item_len):
        item_len = len(value)
print(f"{key_len} is the length of the dict and {item_len} is the min length of the words set")
'''

def hint1():
    return f"key is : {key_n}"
def hint2():
    return f"Last word of the chosen one is :{chosen[-1]}"
def hint3():
    return f"First word of the chosen one is :{chosen[0]}"
def hint4():
    return f"Random word of the chosen one is :{random.choice(chosen)}"
def hint5():
    return f"Mid point words are : {chosen[len(chosen//2)]}"

key_n = random.choice(list(ai_domains))
chosen = random.choice(ai_domains[key_n])

print(" Welcome to the WORD GUESS game... ")
print("Rules are simple.. \n-You have 10 chance to guess it \n-Using hints eats up 20 points")
print("So are you ready?...")
print(key_n, "and the chosen word is ", chosen)

name = input("\nEnter your name :")
print(f"Hello {name} so the length of chosen one is.. ", "_ " * len(chosen))
chance = 0
life = 100
hint_count = 0
hint_key = {1: hint1, 2: hint2, 3: hint3, 4:hint4, 5:hint5}
pl_words =[]
while (chance != 10 and life != 0):
    ask = input("\nWhat could be the world? tell your answer (Hint for Hint)\t").lower()
    if (ask == chosen):
        print(f"WooHoo You won  !!! Rightly chosen {chosen} was the word")
        break
    elif (ask == "hint"):
        hint_count += 1
        life -= 20
        if hint_count in hint_key:
            print(hint_key[hint_count]())
    else:
        print(f"Nope {ask} is not the real word Muahahahaha! ")
        life -=10
    pl_words.append(ask)
    print(f"Hint count : {hint_count} and Life is {life}")

if (life == 0 or chance == 0):
    print(f"You lost Mwahahaha.. having Life: {life} and Chance :{chance}")

print(f"I hope you enjoyed the word was {chosen} \nand your responses were {pl_words} ")