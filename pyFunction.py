def greet_user (name):
  print("Good day, "  + name)

userName = input("What is your name?")
if userName:
  greet_user(userName)

#Challenge 11
#Challenge: Write a function called greet_user that takes a
#parameter called name and prints a personalized greeting message to the user.
# The function should use a default value of 'User' for the name parameter in case no name is provided.
# Call the function with and without a name argument to test it.