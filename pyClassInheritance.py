class Shape:
  def __init__ (self, height, width):
    self.height = height
    self.width = width
  def areaCalc (self):
    raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
  def areaCalc(self):
    return (self.width * self.height)

class Triangle(Shape):
  def areaCalc(self):
    return ((self.width * self.height) / 2)

myRectangle = Rectangle(12, 8)
myTriangle = Triangle(10, 4)

print(f"Rectangle area is: {myRectangle.areaCalc()}")
print(f"Triangle area is: {myTriangle.areaCalc()}")

# Challenge 24
# Create a base class called Shape with a constructor that initializes two instance variables:
# height and width.
# The class should also have a method called area that returns the area of the shape 
# (which should be defined in the subclasses). 
# Then, create two subclasses of Shape called Rectangle and Triangle. 
# The Rectangle class should have a method called area that returns
# the area of a rectangle (height * width),
# while the Triangle class should have a method called area that returns
# the area of a triangle ((height * width) / 2).
# Create instances of both subclasses and call their area methods to verify that they work correctly.