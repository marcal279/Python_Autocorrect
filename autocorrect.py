from accuracy import *

word_file=open('words_alpha.txt','r')
print("Dictionary File being used:",word_file.name)
dict_words=word_file.read()

user_inp=input("Enter a sentence: ")
a=""
for word in user_inp.split():
    print("{}: {}".format(word, (word.lower() in dict_words.split()) ) )
    a=a+" "+ actual_word(word)

if a!=user_inp:
    print("Did you mean:",a.lstrip())


word_file.close()
