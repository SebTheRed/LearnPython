celsiusTemps = [-20, -10, 20, 30, 40]
toFarenheitMap = list(map(lambda num: (num*1.8)+32,celsiusTemps))
trimBelowFreezing = list(filter(lambda num: num>32, toFarenheitMap))
print(trimBelowFreezing)

#Challenge 33
'''
Use map() and a lambda function to convert a list of Celsius temperatures [0, 10, 20, 30, 40]
to Fahrenheit temperatures.
Then, use filter() and a lambda function to filter out all temperatures below 32 degrees Fahrenheit.
'''