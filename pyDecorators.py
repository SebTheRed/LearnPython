import time
current_time = time.gmtime()

timeAssembler = (str(current_time[3]) + ":" + str(current_time[4]))

def decoratorFunction (func):
    def wrapper():
      print("The time is...")
      func()
    return wrapper()

def timeTeller():
   print(timeAssembler)

decoratorFunction(timeTeller)

#Challenge 34
'''
Challenge: Define a decorator function that prints the time before and after a function is called,
along with the time it took to run the function.
Use the time module to get the current time.
Apply this decorator to a function of your choice and test it.
'''
#I kinda get the point of these decorator functions, but it seems like a hat on a hat.