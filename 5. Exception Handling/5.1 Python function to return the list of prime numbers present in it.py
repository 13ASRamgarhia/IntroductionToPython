'''
Given a list of numbers, write a Python function to return the list of prime numbers present in it.

Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]
'''

input_list = [7, 9, 11, 13, 15, 20, 23]

def prime(number):
    if(number == 2):
        return True
    elif(number > 1):
        for i in range(2,(number//2)+1):
            if(number%i == 0):
                return False
        else:
            return True
    else:
        return False

def check_prime(input_list):
    prime_numbers = []

    for number in input_list:
        if(prime(number)):
            prime_numbers.append(number)

    return prime_numbers

print(check_prime(input_list))
