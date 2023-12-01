numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sumTheList (numberList):
  sumNum = 0
  for num in numberList:
    sumNum += num
  return sumNum
  
print(sumTheList(numList))

#Challenge 13
#Write a function that takes a list of integers as input and returns the sum of all the even numbers in the list.