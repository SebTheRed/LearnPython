class BankAccount:
  def __init__ (self, accNum, bal, idNum, name):
    self.accountNumber = accNum
    self.balance = bal
    self.userID = idNum
    self.customerName = name
  def depositMoney (self, val):
    self.balance += val
  def withdrawlMoney (self, val):
    self.balance -= val

sebBel = BankAccount(1234, 1000, 1396, "Sebastian Belfonti")
sebBel.depositMoney(100)
sebBel.withdrawlMoney(10)

print(sebBel.balance)

#Challenge 20 
#Write a Python class for a bank account, with attributes for the account number, balance,
# and account holder's name, and methods for depositing and withdrawing money.