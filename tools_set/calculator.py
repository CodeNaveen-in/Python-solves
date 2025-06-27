print(r"""
   ___________________
  |  _______________  |
  | | CALCULATOR   | |
  | |______________| |
  |  [7][8][9][÷]     |
  |  [4][5][6][×]     |   🧮
  |  [1][2][3][−]     |
  |  [0][.][=][+]     |
  |___________________|

     Crunch those numbers!
""")

def add (n1, n2):
    return n1 + n2

def sub (n1, n2):
    return n1 - n2

def mul (n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

def give_sol(value):
    choice = input("What operation you want to perform? \n + - * / \t:")
    value2 = int(input("Enter your value 2 for input\t:"))
    sol = cal[choice](value, value2)
    print(f"The calculation is {value} {choice} {value2} = {sol} ")
    return sol

def give_res(value):
    res = give_sol(value)
    print(f"Solution of the last calculation is {res}")
    return res

def choice():
    choice = input("\nYou want to continue? yes or no \t:")
    if (choice == "yes"):
        return True
    elif (choice == "no"):
        return False

cal = {"+": add, "-": sub, "*": mul, "/": div}

progOver = False

while (not progOver):
    value1 = int(input("Enter value on 1 for the calculation\t:"))
    result = give_res(value1)
    while (choice()):
        result = give_res(result)
    if (choice() == False): #added a fail safe for fun Haha :)
        ask = input("Enter the escape keyword: ").lower()
        if (ask == "escape"):
            progOver = True