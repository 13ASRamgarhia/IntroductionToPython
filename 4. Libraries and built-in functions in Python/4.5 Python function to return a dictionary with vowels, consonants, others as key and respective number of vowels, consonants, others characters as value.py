'''
Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants, others as key and respective number of vowels, consonants, others characters as value.

Note: Do case insensitive operations

Example: sentence=“I love python and it so easy to learn”
         sample output={“vowels”:12,”consonants”:17, “others”:8}
'''

def vowel_count(sentence):
    Vcount,Ccount,Ocount = 0,0,0
    vowels = ['a','e','i','o','u']
    consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    for letter in sentence.lower():
        if letter in vowels:
            Vcount += 1

        elif letter in consonents:
            Ccount += 1

        else:
            Ocount += 1

    dict = {}
    dict["vowels"] = Vcount
    dict["Consonents"] = Ccount
    dict["Others"] = Ocount

    print(dict)

vowel_count(input("Enter your sentence : "))