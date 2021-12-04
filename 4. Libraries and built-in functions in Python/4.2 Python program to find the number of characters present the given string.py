'''
Write a Python program to find the number of characters present the given string.
'''

def counter(message):
    count = 0

    for letter in message:
        count += 1

    print("-"*20)
    print(f"There are {count} characters in your message")

counter(input("Enter your message : "))