# Challenges

#1. Basic Arithmetic Operations: Create variables a and b, assign them integer values, and perform addition, subtraction, multiplication, and division. Observe the data type of the result in each operation.
a = 67
b = 345
print("Subtraction: ", type(a-b), a-b)
print("Addition: ", type(b+a), b+a)
print("Multiplication: ", type(a*b), a*b)
print("Division: ", type(a/b), a/b)

#2. String Concatenation and Formatting: Create two string variables and concatenate them. Then, use the format() method to insert these strings into another string.
#   Bonus: Try using an f-string for formatting.
str1 = "stringStart"
str2 = "StringEnd"
strConcat = str1 + str2
fVarString = "This string has a variable value of {value:.2f}!"
print(fVarString.format(value = 20.007))

