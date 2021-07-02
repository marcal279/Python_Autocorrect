import itertools as it

#input_word = user input word
#proper_word = word from dictionary

def remove_sames(input_word, proper_word):          #removes same letters so we can find ony points of dissimalrity
    proper_letters=[x for x in proper_word]
    input_letters=[x for x in input_word]
    #print(proper_letters,input_letters)
    
    c=0
    ind=-1 
    while len(proper_letters)>1 and c<15 and ind>=(len(proper_letters) * -1):           
        if input_letters[ind]==proper_letters[ind]:  #-1             
            #print("remove",input_letters[ind])
            proper_letters.pop(ind)
            input_letters.pop(ind)
        else:
            ind=ind-1
        #print(ind)
        c+=1
    return proper_letters,input_letters

def number_of_mismatches(input_word, proper_word):  #total number of letters that dont match in 2 words
    c=0
    for i in range(len(input_word)):
        if input_word[i]!=proper_word[i]:
            c+=1
    return c

def check_adj_keys(input_word, proper_word):        #adjacent key dictionary + checking if mistyped with adjacent dictionary
    adjacent_keys={
        'q':'was',
        'w':'qase',
        'e':'wsdfr',
        'r':'edfgt',
        't':'rfghy',
        'y':'tghju',
        'u':'yhjki',
        'i':'ujklo',
        'o':'iklp',
        'p':'ol',
        'a':'qwsxz',
        's':'aqwedcxz',
        'd':'swerfvcx',
        'f':'dertgbvc',
        'g':'frtyhnbv',
        'h':'bgtyujmn',
        'j':'nhyuikm',
        'k':'mjuiol',
        'l':'mkop',
        'z':'asx',
        'x':'zasdc',
        'c':'xsdfv',
        'v':'cdfgb',
        'b':'vfghn',
        'n':'bghjkm',
        'm':'njkl'
    }
    proper_letters,input_letters=remove_sames(input_word, proper_word)
    if len(proper_letters)==1:
        if proper_letters[0] in adjacent_keys[input_letters[0]]:
            return True
            #print(proper_word)
    return False
    #print("Nopes")

def permut_check(input_word,proper_word):            #check diff permutations of letters of wordd
    proper_letters,input_letters=remove_sames(input_word, proper_word)
    
    if tuple(input_letters) in it.permutations(proper_letters,len(proper_letters)):
        #print(proper_word)
        return True
    else:
        return False
        #print("Nopes")

def letter_accuracy(word,word2):                     #calculates accuracy on letter by letter basis, not used yet
    acc=0.0
    for letter in word:
        #print(letter, word2[word.index(letter)])
        if word2[word.index(letter)]==letter:
            acc+=1.0
    acc=(acc/len(word))*100
    return acc

def actual_word(word):                               #cumulative function that compiles all above functions
    file=open('words_alpha.txt')
    all_words=file.read().split()
    
    if word not in all_words:
        relevant_words=[]
        for x in all_words:
            if len(x)==len(word) and number_of_mismatches(word,x)<3 and (permut_check(word,x) or check_adj_keys(word,x)):
                relevant_words.append(x)
        
        #print(len(relevant_words))
        #print(relevant_words)
        
        if len(relevant_words)==1:
            return relevant_words[0]
        
        else:
            letter_accuracies=[]
            for rel_word in relevant_words:
                letter_accuracies.append([rel_word,letter_accuracy(word,rel_word)])
                letter_accuracies.sort(key=lambda tup: tup[1], reverse=True)  # sorts in place by accuracy, descending order
            return letter_accuracies[0][0]

        #for x in relevant_words:
        #    print("{}; {}: Adj Check={}, Combo Check={}".format(word,x,check_adj_keys(word,x),permut_check(word,x)) )

    else:
        return word
        #print(word,"present in dictionary")
    file.close()



'''
TEST CASES:

print(actual_word('hlelo'), actual_word('jelol'), actual_word('hdllo'))
print(number_of_mismatches('hlelo','aargh'), not permut_check('hlelo','aargh'), not check_adj_keys('hlelo','aargh') )

if permut_check('hello','henlo'):
    print("Combo True")
else:
    print("C False")
if check_adj_keys('hello','hpllo'):
    print("Adjacent True")
else:
    print("Adj False")

word_accuracy('ab')
print(letter_accuracy('hello', 'marcy'))


check_adj_keys('gello','hello')
print(number_of_mismatches('gello','hello'))

permut_check('ehllo','hello')

a,b=remove_sames('hello','eholl')
print(a,b)
'''
