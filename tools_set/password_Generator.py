print(r"""
     ______
    |  __  \___
    | |__) |_  |
    |  ___/ / /    🔐 PASSWORD GENERATOR
    |_|    /_/     Unlock your digital vault!
       ||
   ____||____
  |__________|
""")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passw_list = []
passw = ''

letter_selection = random.sample(letters, nr_letters)
passw_list.extend(letter_selection)

symbol_selection = random.sample(symbols, nr_symbols)
passw_list.extend(symbol_selection)

number_selection = random.sample(numbers, nr_numbers)
passw_list.extend(number_selection)

print(passw_list)

choice = input("What level of password do you want? easy or hard \n")
if (choice == "easy"):
    for i in passw_list:
        passw +=i
    print(f"You can set your password as: {passw} ")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
elif (choice == "hard"):
    random.shuffle(passw_list)
    for i in passw_list:
        passw += i
    print(f"You can use Hard version of the password : {passw}")