'''
Write a Python function generate_fibanacci(n) to return a list of first n Fibonacci numbers.
'''

try:
    def generate_fibonacci(n):
        n1,n2 = 0,1
        print("-"*52)
        for i in range(0,n+1):
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
        print("-"*50)
    generate_fibonacci(n=int(input("Enter the number of fibonacci numbers you want : ")))

except ValueError:
    print("-"*52)
    print("Please enter positive integer only\n")