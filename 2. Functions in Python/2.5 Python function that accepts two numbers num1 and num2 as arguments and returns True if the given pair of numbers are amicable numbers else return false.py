'''
Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false.
Invoke the function and based on return value print the numbers are amicable numbers or not.

num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of num1 is equal to num2 and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.

Example: 220 and 284 are amicable numbers as

Proper devisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284
Proper devisors of 284 are 1, 2, 4, 71, 142 whose sum is 220
'''

def check_amicable_numbers(num1,num2):
    sum1 = 0
    sum2 = 0

    for i in range(1,(num1//2)+1):
        if(num1%i == 0):
            sum1 = sum1 + i

    for j in range(1,(num2//2)+1):
        if(num2%j == 0):
            sum2 = sum2 + j

    if(sum1 == num2 and sum2 == num1):
        return True

    else:
        return False

try:
    num1 = int(input("Enter first number  : "))
    num2 = int(input("Enter second number : "))
    print("-"*40)
    if(check_amicable_numbers(num1,num2)):
        print(f"{num1} and {num2} are amicable numbers")

    else:
        print(f"{num1} and {num2} are NOT amicable numbers")

except ValueError:
    print("-"*40)
    print("Please enter numbers only")