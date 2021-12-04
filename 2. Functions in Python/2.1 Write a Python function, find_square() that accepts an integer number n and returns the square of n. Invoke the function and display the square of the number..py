'''
Write a Python function, find_square() that accepts an integer number n and returns the square of n.
Invoke the function and display the square of the number.
'''

def find_square(n):
     square = n*n

     return square

try:
     n = int(input("Enter a integer : "))
     print("-"*30)
     print(f"Square of {n} is {find_square(n)}")

except ValueError:
     print("-"*30)
     print("Please enter an integer")
