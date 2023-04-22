RED = '\033[31m'
RESET = '\033[0m'
class BankAccount:
  def __init__ (self):
    self.__balance = 100
  def deposit (self, depositAmount):
    self.__balance += depositAmount
  def withdraw (self, withdrawAmount):
    if(self.__balance - withdrawAmount) > 0:
      self.__balance -= withdrawAmount
    else:
      print(RED+ "You cannot withdraw more than your balance" + RESET)
  def get_balance (self):
    return self.__balance

myAccount = BankAccount()
response = int(input("Please choose the ATM function:\n1. Deposit\n2. Withdraw\n3. Get Balance"))
if response == 1:
  depositAmount = int(input("Please enter the amount of $$$ you are depositing today."))
  myAccount.deposit(depositAmount)
  print(myAccount.get_balance())
  print("Is your new balance!")
elif response == 2:
  withdrawAmount = int(input("Please enter the amount of $$ you are withdrawing today."))
  myAccount.withdraw(withdrawAmount)
  print(myAccount.get_balance())
  print("Is your new balance!")
elif response == 3:
  print(myAccount.get_balance())
  print("Is your balance!")
else:
  print("You failed to choose one of the three options. Please re-launch program.")

#Challenge 25
# Create a class called "BankAccount" that has a private attribute called "__balance" initialized to 0.
# Add methods to the class called "deposit" and "withdraw" that allow the balance to be modified,
# but ensure that the balance cannot go below 0.
# Finally, add a method called "get_balance" that returns the current balance.

#Encapsulation is done through access modifiers:
# Three types: public, protected, private.