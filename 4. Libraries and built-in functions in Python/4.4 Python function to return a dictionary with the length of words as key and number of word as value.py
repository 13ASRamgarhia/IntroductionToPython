'''
Write a Python function words_count(sentence) to return a dictionary with the length of words as key and number of word as value.

Example: sentence=“I am Amandeep Singh” sample output={1: 1, 2: 2, 8: 3, 5: 4}
'''

sentence = input("Enter your sentence : ")

def words_count(sentence):
    splitted_sentence = sentence.split(" ")
    dict = {}

    for word in splitted_sentence:
        length = len(word)
        posi = splitted_sentence.index(word)+1
        dict[length] = posi
    print("-"*21)
    print(dict)

words_count(sentence)