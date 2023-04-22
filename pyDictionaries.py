sentenceInput = input("Please enter a long sentence.")
splitSentence = sentenceInput.split()
wordCountDict = {word: 0 for word in splitSentence}
for word in splitSentence:
    wordCountDict[word] += 1

print(wordCountDict)

#Challenge 27
# Write a Python program that prompts the user to enter a sentence
# and then creates a dictionary where the keys are the words in the sentence
# and the values are the number of times each word appears in the sentence.
# The program should then print the dictionary.

#Dictionaries are just objects
'''
List of Dictionary operators:
- emptyDictionary = dict() #Establishes an empty dictionary.
- dictVar["key"] #Will return the corresponding value of the pair.
- dictVar.get("key") #Does the same thing as above, but will return "None" if the key is missing.
- dictVar["newKey"] = "newValue" #Sets or changes a new or existing dictionary Key/Value pair.
- del dictVar["key to be deleted"] #Will remove that K/V pair.
- dictVar.pop("key to be deleted") #Does the same thing as above.
- dictVar.keys() #Prints a list(array) of all the keys. Values not included.
- dictVar.values() #Prints a list(array) of all the values. Keys not included.
- dictVar.items() #Returns a list of tuples (??)
'''