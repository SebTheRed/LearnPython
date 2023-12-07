# Challenges:

# String Combination Task:
# Write a Python program to combine two strings str1 and str2 into a single string, separated by a hyphen. For instance, if str1 is "Hello" and str2 is "World", the output should be "Hello-World".
str1 = "Hello"
str2 = "World"
concatString = str1 + "-" + str2
print(concatString)

# Simple Slicing Task:
# Given a string sentence, write a Python function that returns the first and the last 3 characters of that string as a single string. If the length of the string is less than 3, return the original string.

def extract_characters(sentence):
  senLen = len(sentence)
  senLenMusThree = senLen-3
  if senLen < 3:
    return(sentence)
  front3 = sentence[0:3]
  back3 = sentence[senLenMusThree:senLen]
  sixString = front3 + back3
  return sixString

print("Hello Python: ", extract_characters("Hello Python"))
print("Hi: ", extract_characters("Hi"))