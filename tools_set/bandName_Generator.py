print(r"""
  ____                  _ ____                      _             
 |  _ \ __ _ _ __   ___| | __ )  ___  __ _ _ __ ___| |__   ___ _ __ 
 | |_) / _` | '_ \ / _ \ |  _ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
 |  __/ (_| | | | |  __/ | |_) |  __/ (_| | | | (__| | | |  __/ |   
 |_|   \__,_|_| |_|\___|_|____/ \___|\__,_|_|  \___|_| |_|\___|_|   

          🎶  RANDOM BAND NAME GENERATOR 🎵
     From punk to pop, let fate name your next hit!
""")
#To greet the user
name= input("What is your name? : ")
print("Hello "+ name + " ! Welcome to Band Generator")

#To ask for city and pet name
city_name = input("What is your Hometown city name? ")
pet_name = input("So What is your pet name? : ")

#Concatenate the results of the queries
print("Your Band Name will be - " + city_name + pet_name)