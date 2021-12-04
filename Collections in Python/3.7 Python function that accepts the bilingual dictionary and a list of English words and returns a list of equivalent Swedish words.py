'''
Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary

{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

and use it to translate your Christmas wishes from English into Swedish.
That is, write a Python function translate(b_dict,list_words) that accepts the bilingual dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words.
'''

eng_wish = input("\nEnter your christmas wish : ")
eng_wish_l = eng_wish.lower()
list_words = eng_wish_l.split(" ")
b_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(b_dict,list_words):
    swedish_wish = []

    for word in list_words:
        for key in b_dict:
            if(word == key):
                swedish_wish.append(b_dict[key])

    return swedish_wish

print("-"*40)
for word in translate(b_dict,list_words):
    print(word,end = " ")