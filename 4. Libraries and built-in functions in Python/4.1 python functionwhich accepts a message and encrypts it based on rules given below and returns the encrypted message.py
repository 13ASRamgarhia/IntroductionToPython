'''
Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below and returns the encrypted message.

Words at odd position  -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.

Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea
'''
import re

original_msg = input("Enter your message to encrypt : ")
msg = original_msg.split()
vowels = ['a','e','i','o','u']

if(re.search(r"\d",original_msg)):
    print("-"*31)
    print("Please enter your message in letters only")

else:
    def encrypt_message(msg):
        encrypted_message = []

        for index,word in enumerate(msg):
            if((index+1)%2 != 0):
                encrypted_message.append(word[::-1])

            else:
                c = []
                v = []
                for letter in word:
                    if letter in vowels:
                        v.append(letter)
                    else:
                        c.append(letter)

                c.extend(v)
                encrypted_message.append("".join(c))

        return " ".join(encrypted_message)


    print("-"*31)
    for word in encrypt_message(msg):
        print(word,end = "")