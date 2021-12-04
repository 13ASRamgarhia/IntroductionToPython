'''
Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false.
Invoke the function and based on return value print the output.

Example: num=12321 output: Given number is a palindrome, num=12345 output: Given number is not a palindrome
'''

def is_palindrome(num):
    string = str(num)

    if(string == string[::-1]):
        return True

    else:
        return False

try:
    num = int(input("Enter the number to check : "))
    print("-"*35)
    if(is_palindrome(num)):
        print(f"{num} is a palindrome")

    else:
        print(f"{num} is NOT a palindrome")

except ValueError:
    print("-"*35)
    print("Please enter a positive integer")

