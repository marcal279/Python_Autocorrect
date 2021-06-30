# Python_Autocorrect
Autocorrect system using Python

CURRENT
Created an autocorrect system; not real time, after a line typed, come up with suggestions for the line like 
'Did you mean: [corrected spelling of the word]'
If user puts in no, then it provides option to add to dictionary

STEPS
1. Import a dictionary, word meaning pairs
2. Enter line from user
3. Check each word against dictionary
4. Calculate accuracy of mistyped words using length and adjacent keyboard keys; can also see diff combinations, so 'as' can be accepted
error for 'sa'
5. See similarity to words in dictionary
6. Max similarity words printed/suggested as correction

TO ADD:
1. Modify dictionary so words are saved along with FREQUENCY of usage, suggest using .json file instead of .txt 

MOST IMP Functions:
1. Word accuracy function/ calculation of error
2. Compiling the adjacent keys dictionary

Additional later features:
1. Start learning common mistakes of the user by seeing frequency of wrong alphabet (eg: user usually makes mistake of typing s instead of a)
2. Based on above, start autocompletion/autosuggestions
3. Develop typing application, calculating typing speed, word accuracy
4. Different languages
