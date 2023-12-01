class Person:
  species = "Homo sapiens"
  def __init__ (self, name, age):
    self.name = name
    self.age = age
  
seb = Person("Sebastian", 27)
chatBot = Person("chatGPT", 13)

print(seb.species)
print(Person.species)

#Challenge 23
# Create a class Person with a class attribute species set to "Homo sapiens".
# Then create two instances of Person with different instance attributes (e.g. name, age).
# Print out the species attribute for each instance.