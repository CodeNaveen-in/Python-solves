#Greet the user
print("Hello User, Welcome to the BILL CALCULATOR")

#Ask for the total bill
total_bill = int(input("Give us the total bill amount: $"))

#Ask for tip percent
tip_choice=int(input("How much would you like to tip? 10, 12, 15 or more?? "))

#Ask for no of people
people_num = int(input("How many of people are paying? "))

#Calculate per person share and Give back the bill amount
pps = str(round(total_bill* (1 + tip_choice/100) / people_num,2))
print("The amount per person had to give is $" + pps)