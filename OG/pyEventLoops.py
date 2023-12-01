import asyncio

async def sumNumFunc(num):
    sumList = []
    for i in range(num):
        sumList.append(i + num)
    return sumList
    

inputInt = int(input("Please input an integer."))
returnVal = asyncio.run(sumNumFunc(inputInt))
print(returnVal)
#Challenge 38
'''
Write a program that prompts the user to enter a positive integer
and calculates the sum of all even numbers between 1 and that integer, inclusive.
Use asyncio and await to implement the program with a coroutine.
'''
