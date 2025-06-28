# Format: (water_ml, coffee_g, milk_ml)
coffee_menu = {
    "espresso": {
        "ingredients": {"water_ml": 30, "coffee_g": 18, "milk_ml": 0},
        "desc": "Bold & concentrated",
        "$": 0.8
    },
    "latte": {
        "ingredients": {"water_ml": 30, "coffee_g": 18, "milk_ml": 150},
        "desc": "Creamy & mellow",
        "$": 2.8
    },
    "cappuccino": {
        "ingredients": {"water_ml": 30, "coffee_g": 18, "milk_ml": 120},
        "desc": "Foamy & balanced",
        "$": 2.5
    },
    "americano": {
        "ingredients": {"water_ml": 150, "coffee_g": 18, "milk_ml": 0},
        "desc": "Smooth & smoky",
        "$": 1.3
    },
    "flat white": {
        "ingredients": {"water_ml": 30, "coffee_g": 18, "milk_ml": 120},
        "desc": "Strong & silky",
        "$": 2.3
    }
}

machine_stats = {
        "ingredients": {"water_ml": 1000, "coffee_g": 200, "milk_ml": 1000},
        "order":[],
        "$": 0
        }

def order_pos(order):
    """Checks if the machine have sufficient ingredient and returns either ingredients or none"""
    machine_ing = machine_stats["ingredients"]
    order_ing = coffee_menu[order]["ingredients"]
    water_left = machine_ing["water_ml"] - order_ing["water_ml"]
    coffee_left = machine_ing["coffee_g"] - order_ing["coffee_g"]
    milk_left = machine_ing["milk_ml"] - order_ing["milk_ml"]

    if (water_left > 0 and coffee_left > 0 and milk_left > 0):
        return (water_left, coffee_left, milk_left)

def count_mon (mon):
    count = 0
    return mon["dollar"] + mon["quarter"]*0.25 + mon["dime"]*0.10 + mon["nickel"]*0.05 + mon["pennies"]*0.01

def mon_check(order, money):
    price = coffee_menu[order]["$"]
    if (money >= price):
        return money - price
    else:
        return -1 #again same problem if - if failed it gave none which clashed with 0 comparison of price

print("Hey there welcome to the NAVEEN COFFEE SHOP....")
choice = input("What would you like? : Coffee or Report? :\t").lower()
while (choice == "coffee"):
    print ("We have orders such as: ")
    for i in coffee_menu:
        print(f" - {i.capitalize()} which is {coffee_menu[i]["desc"]} at the price of ${coffee_menu[i]["$"]}")
    order = input("Enter your coffee order\t:").lower()
    fes = order_pos(order)
    if (fes): #if order fails it gives none, which is not true so if doesn't go through - NEW TRICK LEARNED
        mon = {"dollar": 0, "quarter":0, "dime": 0, "nickel": 0, "pennies": 0}
        for money, num in mon.items():
            num = int(input(f"Enter your {money} : "))
            mon[money] = num
        count = count_mon(mon)
        money_left = mon_check(order, count)
        if ( money_left >= 0):
            print("Here's your coffee")
            machine_stats["ingredients"]["water_ml"] = fes[0]
            machine_stats["ingredients"]["coffee_g"] = fes[1]
            machine_stats["ingredients"]["milk_ml"] = fes[2]
            machine_stats["order"].append(order)
            machine_stats["$"] += coffee_menu[order]["$"]
            if (money_left > 0):
                print (f"Here's your remaining balance : {money_left}")
        else:
            print("Sorry the money added is insufficient, your transaction is cancelled")
    else:
        print(f"Sorry, We can't make your coffee we are lacking on ingrdients {machine_stats['ingredients']}")
    choice = input("What would you like? : Coffee or Report? :\t").lower()
if (choice == "report"):
    print(machine_stats)