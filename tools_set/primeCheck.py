print(r"""
      _______
     /  ___  \ 🔍
    |  | P |  |
    |  | R |  |   Prime Checker
    |  | I |  |   Inspecting integers...
     \_| M |_/
        | |
       (___)
""")

def primeCheck(num):
    if (num <2):
        return f"NOPE! Not a prime {num} is not prime"
    elif (num == 2 or num == 3):
        return f"{num} is prime as it has no other factor other than 1 and {num}"
    elif (num>3):
        factor = []
        root = int((num ** 0.5) + 1)
        for i in range(2,root):
            if (num % i == 0):
                print(f"It is composite number as {i} is also a factor of {num}")
                factor.append(i)
                counterpart = num//i
                if (counterpart != i):
                    factor.append(counterpart)
        if (not factor):
            return f"The number {num} is a prime number as it as no factors other than 1"
        else:
            return f"The Number {num} as it has numerous factors list is : {sorted(factor)}"

while (True):
    num = int(input("Hey yo what number you want to check prime nature of? "))
    out = primeCheck(num)
    print(out)
    ask = input("Want to check more? enter escape code if not: ").lower()
    if (ask == "escape"):
        break