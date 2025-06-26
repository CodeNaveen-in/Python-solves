def is_leap_year(year):
    if (year%4 == 0):
        if (year%100 == 0):
            if (year%400 == 0):
                return True
            else:
                return False
        else:
            return True
    return False

print("Hello and welcome to the LEAP YEAR CHECKER")
year = int(input("Enter your year to check :\t"))
out=is_leap_year(year)

if (out == True):
    print(f"{year} is a leap year.")
else:
    print(f"Sadly the {year} is not a leap year")