'''
Write a Python program to find and display the maximum of three given numbers
'''

try:
    num1 = float(input("Enter first number  : "))
    num2 = float(input("Enter second number : "))
    num3 = float(input("Enter third number  : "))
    print("-" * 35)

    if(num1 != num2 and num1 != num3 and num2 != num3):
        if(num1>num2):
            if(num1>num3):
                print(f"{num1} is the maximum")
            else:
                print(f"{num3} is the maximum")

        else:
            if(num2>num3):
                print(f"{num2} is the maximum")
            else:
                print(f"{num3} is the maximum")
    else:
        print("Please enter three numbers without repetation")

except ValueError:
    print("-" * 35)
    print("Please enter numbers only")