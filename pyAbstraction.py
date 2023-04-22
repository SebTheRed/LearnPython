from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def eat (self):
    pass
  @abstractmethod
  def speak (self):
    pass

class Cat(Animal):
  def __init__ (self, cuteOrUgly):
    self.cuteOrUgly = cuteOrUgly
  def eat(self):
    return f"This cat is {self.cuteOrUgly} while its eating."
  def speak(self):
    return "Cats can't speak."

class Dog(Animal):
  def __init__ (self, cuteOrUgly):
    self.cuteOrUgly = cuteOrUgly
  def eat(self):
    return f"The Dog is eating kinda {self.cuteOrUgly}.."
  def speak(self):
    return "Dogs can't speak."

myCat = Cat("cute")
uglyDog = Dog("ugly")

print(myCat.eat(), myCat.speak())
print(uglyDog.eat(), uglyDog.speak())

#Challenge 26
# Create an abstract class called Animal with two abstract methods speak and eat.
# Then create two classes Dog and Cat that inherit from Animal
# and implement the speak and eat methods in their own way.
# Finally, create an object of each class and call their methods.

# An abstract class is a class
# that cannot be instantiated and is only used as a base class for other classes.

#I 100% do not get why this is necessary.