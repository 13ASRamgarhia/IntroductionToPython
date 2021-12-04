'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding.
Repetition of character has to be replaced by storing the length of that run.

Write a python function encode(message)  which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program.

Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C
'''

message = input("Enter a message : ")
print("-"*25)

if(message.isalpha() and message.isupper()):
    def encode(message):
        pairs = []
        for char in message:
            if len(pairs) > 0:
                if pairs[-1][0] == char:
                    pairs[-1] = (char, pairs[-1][1] + 1)
                else:
                    pairs.append((char, 1))
            else:
                pairs.append((char, 1))
        strings = []
        for letter, count in pairs:
            strings.append(f"{count}{letter.upper()}")
        return "".join(strings)

    print(encode(message))

else:
    print("Please enter message in uppercase letters only")