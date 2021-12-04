'''
Write a Python program that displays a message as follows for a given number:

- If it is a multiple of 3, display "Zip"
- If it is a multiple of 5, display "Zap"
- If it is a multiple of both 3 and 5, display "Zoom"
- If it does not satisfy any of the above given conditions, display "Invalid"
'''

try:
    num = int(input("Enter the number : "))
    print("-"*25)
    if(num%3 == 0):
        print("Zip")

    elif(num%5 == 0):
        print("Zap")

    elif(num%3 == 0 and num%5 == 0):
        print("Zoom")

    else:
        print("Invalid")

except ValueError:
    print("-" * 25)
    print("Please enter a positive number")
