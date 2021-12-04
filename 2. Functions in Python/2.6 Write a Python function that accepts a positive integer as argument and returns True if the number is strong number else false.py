'''
Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True if the number is strong number else false.
Invoke the function and based on return value print the number is strong number or not.

A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.

Example:145 is strong number as
1!=1
4!=24
5!=120
Sum of all these is 145
'''

def factorial(r):
    fac = 1

    while(r>0):
        fac = fac * r
        r -= 1

    return fac

def check_strong_number(num):
    sum = 0

    while(num>0):
        r = num%10
        sum = sum + factorial(r)
        num = num//10

    return sum

try:
    num = int(input("Enter a positive integer : "))
    temp = num
    print("-" * 40)

    if(temp>0):
        if(check_strong_number(num) == temp):
            print(f"{num} is a strong number")
        else:
            print(f"{num} is NOT a strong number")
    else:
        print("Please enter a positive integer")

except ValueError:
    print("-"*40)
    print("Please enter a positive integer")