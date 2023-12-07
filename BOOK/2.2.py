# Notes:
# Python has 6 types of operators:
# Arithmetic, Comparison, Logical, Assignment, Identity, Membership
# Arithmetic is your math operators.
# Comparison is discerning the difference between values.
# Logical is simply three methods (and, or, not) that checks between boolean values.
# Assignment gives a variable its value, additional arithmetic can be included.
# Identity is used to determine if an object is the same as itself. simply (is, is not) operators.

#1. Exploring Arithmetic Operators: Create two variables and use each arithmetic operator. Experiment with different values (including negative numbers and zero).
a = 67
b = 27
print("Subtraction: ", type(a-b), a-b)
print("Addition: ", type(b+a), b+a)
print("Multiplication: ", type(a*b), a*b)
print("Division: ", type(a/b), a/b)

#2. Logical Puzzles: Given three boolean variables x, y, and z, write expressions using logical operators that return True only if exactly two of the three variables are True.
x = True
y = False
z = True

result = (x and y and not z) or (x and not y and z) or (not x and y and z)
print(result) 