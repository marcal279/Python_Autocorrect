from accuracy import *

word_file=open('Github\Python Autocorrect\words_alpha.txt','r')
print("Dictionary File being used:",word_file.name)
dict_words=word_file.read()

user_inp=input("Enter a sentence: ")
a=""
for word in user_inp.split():
    print("{}: {}".format(word, (word.lower() in dict_words.split()) ) )
    a=a+" "+modified_acc(word)

if a!=user_inp:
    print("Did you mean:",a)


word_file.close()