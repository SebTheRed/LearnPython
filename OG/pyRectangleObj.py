class Rectangle:
  def __init__ (self, width, height):
    self.height = height
    self.width = width
  def calcArea (self):
    area = self.width * self.height
    return area

inputNum1 = int(input("Please enter first number."))
inputNum2 = int(input("And now the second number, please!"))
rectangle1 = Rectangle(inputNum1, inputNum2)
print(rectangle1.calcArea())


#Challenge 21
# Define a Rectangle class with attributes width and height and a method area that
# calculates and returns the area of the rectangle.
# Then create an object of the Rectangle class and call the area method on it.