'''
Write a Python program to find the sum of digits of a given number.

Example: Sum of digits of the number 123 will be 6
Note: Initialize the number with various values and test your program.
'''
try:
    num = int(input("Enter the number : "))
    sum = 0
    temp = num
    number = abs(num)
    while(number > 0):
        n = number%10
        sum += n
        number = number//10

    print("-"*33)
    print(f"Sum of digits of {temp} is {sum}",)

except ValueError:
    print("-" * 33)
    print("Please enter a positive number")