listONums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lambdaFunction = lambda list: [num for num in list if num%2 == 0]
print(lambdaFunction(listONums))

#Challenge 32
# Write a lambda function that takes a list of numbers and returns a new list with only the even numbers.
# Test your function with a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].