'''
Write a Python program to print first n Fibonacci numbers.
'''

try:
    n = int(input("Enter number till you want Fibonacci series : "))
    print("-" * 49)
    n1, n2 = 0, 1
    counter = 0

    if(n <= 0):
        print("Please enter a positive integer")

    elif(n == 1):
        print(f"Fibonacci Series : {n1}")

    else:
        print("Fibonacci Series : ",end = "")
        while(counter < n):
            print(n1, end="  ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            counter += 1

except ValueError:
    print("-"*49)
    print("Please enter a positive integer")