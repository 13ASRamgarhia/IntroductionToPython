'''
Write a python function find_common_characters(msg1,msg2) to display all the common characters between given two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
Example: msg1="I like Python", msg2="Java is a very popular language" output=lieyon
'''

msg1 = "I like Python"
msg2 = "Java is a very popular language"

def find_common_characters(msg1,msg2):
    space = " "
    common_char = []

    for letter1 in msg1:
        if(letter1 != space):
            for letter2 in msg2:
                if(letter1 == letter2):
                    common_char.append(letter1)
                    break

    return common_char

common_characters = find_common_characters(msg1,msg2)

print(msg1)
print(msg2)
print("-"*30)

if(len(common_characters) == 0):
    print("-1")
else:
    for char in common_characters:
        print(char,end = "")