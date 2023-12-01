import asyncio

async def async_sleep(n, msg):
    await asyncio.sleep(n)
    print("\033[31m" + msg + '\033[0m')

inputString = str(input("Please provide a sentence."))
inputNum = int(input("Please provide an integer."))

asyncio.run(async_sleep(inputNum, inputString))

# Challenge 36
'''
Write a Python function async_sleep that takes an integer n as input
 and uses the asyncio.sleep function to sleep for n seconds.
   The function should be declared as asynchronous using the async keyword,
     and should use the await keyword to call the asyncio.sleep function.
'''