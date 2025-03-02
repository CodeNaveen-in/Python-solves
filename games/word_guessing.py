import random

#Guiding user
print("Hello user, we are at word guessing game")
name=input("Name please ..  ")
print(f"{name} the aim is that you have to guess which was the word the computer has chosen..")

#Solution word choosing
words=["Apple", "Bamboo", "Cat", "Domain", "Enigma", "Fable", "Grandiose", "Helicopter"]
sol_word = words[random.randint(0, len(words)-1)]

#Hint presenting and game start
print(f"The Game has started : \n Word is {sol_word[0]}" + (len(sol_word)-1) * '*' )
guess = ''

#Guess and evaluation starts
print(sol_word)
for char in sol_word:
    if guess in sol_word:
        print (sol_word[0] + char)
    else:
        print (sol_word[0] + "-")
    guess = input()