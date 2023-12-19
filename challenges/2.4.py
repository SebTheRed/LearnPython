import random
# Challenges:
class InputChallenges:
  def __init__(self):
    self.idk = "idk"
# Calculator for Basic Operations:
# Create a simple calculator that accepts two numbers and an operator (+, -, *, /) from the user and performs the operation.
  def calculator():
    numOne = int(input("Enter the first number: "))
    operand = str(input("Enter an operator (+, -, *, /): "))
    numTwo = int(input("Enter the second number: "))
    if operand == "+":
      print("result: ", numOne + numTwo)
    elif operand == "-":
      print("result: ", numOne - numTwo)
    elif operand == "*":
      print("result: ", numOne * numTwo)
    elif operand == "/":
      print("result: ", numOne / numTwo)
    else: print("Operation failed, please only use the operators provided.")
# Guess the Number Game:
# Write a program where the user has to guess a predetermined number. After each guess, inform the user whether their guess was too high, too low, or correct.
  def numberGuesser():
    randomNum = int(random.randint(1,10))
    print("Guess a number between 1 and 10!")
    guessNum = int(input("Input number: "))
    while guessNum != randomNum:
      if guessNum > randomNum:
        print("Your guess was greater than the number. Try again!")
        guessNum = int(input("Input another number: "))
      else:
        print("Your guess was lower than the number. Try again!")
        guessNum = int(input("Input another number: "))
    print("You guessed correctly! The number was: ", "\033[32m"+str(randomNum)+"\033[0m")


chosenChallenge = int(input("Input 1 for calculator. Input 2 for guessing game..."))
if chosenChallenge == 1:
  InputChallenges.calculator()
elif chosenChallenge == 2:
  InputChallenges.numberGuesser()