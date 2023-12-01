myNum = 5

def change_num():
  global myNum
  myNum = 10
  print(myNum)

change_num()

#Challenge 15
#Create a global variable my_num and set it to 5. 
#Write a function change_num() that takes no arguments and changes the value of my_num to 10. 
#Print the value of my_num before and after calling the change_num() function

#It is bad practice to use global variables in larger apps.