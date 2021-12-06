'''
Write a Python function words_count(sentence) to return a dictionary with the length of words as key and number of words with such length as value.

Example: sentence=“I love python and it is so easy to learn” sample output={1: 1, 4: 2, 6: 1, 3: 1, 2: 4, 5: 1}
'''

sentence = input("Enter your sentence : ")

def words_count(sentence):
    splitted_sentence = sentence.split(" ")
    dict = {}
    count = 0

    for word1 in splitted_sentence:
        length = len(word1)
        for word2 in splitted_sentence:
            if(len(word1) == len(word2)):
                count += 1

        dict[length] = count
        count = 0
    print(dict)

words_count(sentence)
