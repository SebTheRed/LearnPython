listOne = [1, 2, 3, 4, 5]
listTwo = [0, 2, 4]
listThree = [-2, -10, 5]

RED = '\033[31m'
RESET = '\033[0m'

def listChecker (listGiven):
  for num in listGiven:
    if num < 0:
      raise (RED+ "All numbers should be positive!" + RESET)

listChecker(listThree)

#Challenge 19
#Write a function in Python that takes a list of numbers as input and raises a custom exception
# if the list contains any negative numbers. The custom exception should be defined as
# a separate class and should include a message stating that negative numbers are not allowed.
# Finally, test your function with a few different lists containing both positive and negative numbers.