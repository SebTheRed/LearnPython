import random
import asyncio

async def randomNumFunc ():
    randomNumList = []
    for i in range(10):
        rando = random.randint(1, 100)
        randomNumList.append(rando)
    return randomNumList
async def randoSquares():
    squaresList = []
    randomNumList = await randomNumFunc()
    for i in randomNumList:
        squaresList.append(i*i)
    return squaresList

async def mainFunc():
    result = await asyncio.gather(randoSquares())
    print('\033[32m'+ str(result) + '\033[0m')
asyncio.run(mainFunc())

# Challenge 37
'''
Write a Python program that creates a list of 10 random numbers between 1 and 100.
Then, use asyncio and the asyncio.gather() function to calculate
the square root of each number in the list.
Finally, print out the list of square roots.
'''