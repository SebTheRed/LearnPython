favFoodsInput = input("Enter your favorite foods with commas between\nExample: Pizza, Glizzies, Chipotle\n")
splitFoods = favFoodsInput.split(",")
favFoodTuple = tuple(food for food in splitFoods)
print(favFoodTuple)


#Challenge 29
# Write a Python program that creates a tuple of your favorite foods,
# and then prints out the third element of the tuple.