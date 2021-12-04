'''
Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.

Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
'''

try:
    def proper_divisors(num):
        print("-"*50)
        proper_div = []

        if(num>0):
            for i in range(1,(num//2)+1):
                if(num%i == 0):
                    proper_div.append(i)
        else:
            print("Please enter positive integer only")

        return proper_div

    print("-"*50)
    prop_div = proper_divisors(num=int(input("Enter a number : ")))

    for divisor in prop_div:
        if(divisor == prop_div[-1]):
            print(divisor,end = "")
        else:
            print(divisor,end = ", ")

except ValueError:
    print("-"*50)
    print("Please enter positive integer only")