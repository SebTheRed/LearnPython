# CHALLENGE:
# Defines a variable temperature and assigns it a value.
# Uses if-elif-else statements to print different messages based on the temperature:
# Below 0: "It's freezing!"
# 0 to 15 degrees: "It's cold!"
# 16 to 25 degrees: "It's nice and comfortable."
# Above 25 degrees: "It's hot!"
# Change the value of temperature to test different conditions.

temp = int(input("What's the temperature outside? Yes go outside and touch grass."))

if temp < 0:
  print("It's freezing! All of the grass is dead!")
elif temp <= 15:
  print("It's cold!")
elif temp <= 25:
  print("It's nice!")
else:
  print("It's hot!")