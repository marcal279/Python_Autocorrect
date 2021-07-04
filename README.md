# Python_Autocorrect
Autocorrect system using Python

CURRENT:
Created an autocorrect system; not real time, after a line typed, come up with suggestions for the line like 
'Did you mean: [corrected spelling of the word]'


STEPS:
1. Import a dictionary, compilaion of words
2. Enter line from user
3. Check each word against dictionary
4. Calculate accuracy of mistyped words using length and adjacent keyboard keys; can also see diff combinations, so 'as' can be accepted
error for 'sa'
5. See similarity to words in dictionary
6. Max similarity words printed/suggested as correction


PROBLEMS:
Due to expansiveness of dictionary used right now, several words that are not frequently used but still valid (presnt in dictionary) come as suggestion


TO ADD Additional later features:
1. Modify dictionary so words are saved along with FREQUENCY of usage, suggest using .json file instead of .txt
2. Start learning common mistakes of the user by seeing frequency of wrong alphabet (eg: user usually makes mistake of typing s instead of a)
3. Based on above, start autocompletion/autosuggestions
4. Develop typing application, calculating typing speed, word accuracy
5. Different languages
6. Option to add unknown words to dictionary
