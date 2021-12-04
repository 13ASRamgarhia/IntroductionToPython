'''
Write a Python function, find_sum() that accepts an integer n and returns the sum of first n numbers.
Invoke the function and display the sum of first n numbers.
'''

def find_sum(n):
    sum = 0
    n1 = abs(n)
    while(n1>0):
        m = n1%10
        sum += m
        n1 = n1//10

    return sum

try:
    n = int(input("Enter an integer : "))
    print("-"*32)
    print(f"Sum of first {n} integers in {find_sum(n)}")

except ValueError:
    print("-"*32)
    print("Please enter an postive integer")