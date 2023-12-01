import asyncio

async def readFileCoRoutine ():
    fileVar = open("input.txt", "r")
    fileContents = fileVar.read()
    return fileContents

async def mainFunc ():
    result = await readFileCoRoutine()
    print(result)

asyncio.run(mainFunc())

#Challenge 35
#Write a coroutine that reads data from a file
# and sends it to another coroutine that processes the data.