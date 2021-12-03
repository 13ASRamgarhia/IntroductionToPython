def prime_num(num):

    if(num > 1):
        for i in range(2,(num//2)+1):
            if(num%i == 0):
                return False
                break
        else:
            return True


try:
    num = int(input("Enter a number : "))
    print("-"*35)
    if(prime_num(num)):
        print(f"{num} is a prime number")
    else:
        if (num <= 1):
            print(f"{num} is NOT a prime number")

        else:
            print(f"{num} is NOT a prime number")

except ValueError:
    print("Please enter a positive integer")

