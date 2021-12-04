'''
Python function factorial(num) which returns the factorial of a given number.
'''

def factorail(num):
    fac = 1
    n = abs(num)

    if(n>0):
        while(n>0):
            fac = fac * n
            n -= 1

    return fac

try:
    num = int(input("Enter a number : "))
    print("-"*35)
    if(num>0):
        print(f"Factorial of {num} is {factorail(num)}")

    elif(num<0):
        num1 = abs(num)
        if(num1%2 == 0):
            print(f"Factorial of {num} is {factorail(num)}")
        else:
            print(f"Factorial of {num} is -",end = "")
            print(factorail(num))

    else:
        print(f"Factorail of {num} is 1")

except ValueError:
    print("-"*35)
    print("Please enter an integer")