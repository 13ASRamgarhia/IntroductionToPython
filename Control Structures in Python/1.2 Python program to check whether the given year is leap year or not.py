'''
Python program to check whether the given year is leap year or not
'''
try:
    year = int(input("Enter year to check : "))
    print("-"*27)
    if(year%4 == 0):
        print(f"{year} is a leap year")

    else:
        print(f"{year} is NOT a leap year")

except ValueError:
    print("-"*27)
    print("Please enter a valid year")