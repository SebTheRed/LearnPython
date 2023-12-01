class Car:
  def __init__ (self):
    self.make = "Subaru"
    self.model = "Impreza"
    self.year = 2020

myCar = Car()
myCar.make = "Chevy"
myCar.model = "Corvette"
myCar.year = "2022"

print([myCar.make, myCar.model, myCar.year])

#Challenge 22
#Create a class called Car with the instance attributes make, model, and year.
# Instantiate an instance of the class and set the attributes to values of your choice.
# Then, print out the attribute values to confirm that they were set correctly.

#Note: The self.variables in classes are called
#INSTANCE ATTRIBUTES!