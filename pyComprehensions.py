listONums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
setONums = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
tupleONums = (21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

multiThreeList = [num for num in listONums if num%3 == 0]
multiThreeSet = {num for num in setONums if num%3==0}
multiThreeTuple = tuple(num for num in tupleONums if num%3==0)
print(multiThreeList)
print(multiThreeSet)
print (multiThreeTuple)

# Challenge 30
# Write a list comprehension that creates a list of the first 10 multiples of 3.
# Instead I'm going to do that multiples of 3 thing on the 3 different collection types.

