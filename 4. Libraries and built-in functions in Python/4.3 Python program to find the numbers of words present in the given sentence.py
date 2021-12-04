'''
Write a Python program to find the numbers of words present in the given sentence.
'''

#Check it with input - My name is Amandeep Singh and I am 21 years old
def counter(msg):
    msg_list = msg.split()
    count = 0

    for word in msg_list:
        word1 = str(word)
        if(word1.isalpha()):
            count += 1

    print("-"*21)
    print(f"There are {count} words in your sentence")

counter(input("Enter your sentence : "))