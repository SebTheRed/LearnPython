import traceback

inputNum1 = int(input("Please enter the first number you'd like to divide."))
inputNum2 = int(input("Please enter the second number you'd like to divide by."))

RED = '\033[31m'
RESET = '\033[0m'

try:
  dividedNum = inputNum1 / inputNum2
  print(dividedNum)
except:
  print(RED + "ERROR")
  traceback.print_exc()
  print(RESET)

#Challenge 18
# Write a Python function that prompts the user to enter two numbers,
# divides the first number by the second number,
# and prints the result. Use a try-except block to handle any exceptions that might occur.
# If an exception occurs,
# print an error message indicating the nature of the exception.

#ALL ERRORS:
'''
ZeroDivisionError:   Raised when division or modulo by zero is performed.
TypeError:   Raised when an operation or function is applied to an object of inappropriate type.
ValueError:   Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
IndexError:  Raised when an index is not found in a sequence.
KeyError:  Raised when a key is not found in a dictionary.
NameError:   Raised when a local or global name is not found.
AttributeError:  Raised when an attribute reference or assignment fails.
IOError:   Raised when an I/O operation (such as reading or writing to a file) fails.
ImportError:  Raised when an import statement fails to find the module definition or when a from ... import statement fails to find a name that is to be imported.
RuntimeError:   Raised when an error is detected that doesn't fall in any of the other categories.
NotImplementedError:  Raised when an abstract method that needs to be implemented in a subclass is not actually implemented.
KeyboardInterrupt:   Raised when the user hits the interrupt key (usually Control-C or Delete).
FileNotFoundError:   Raised when a file or directory is requested but doesn't exist.
StopIteration:   Raised when the iterator has no more items.
IndentationError:  Raised when there is an incorrect indentation in the code.
SyntaxError:   Raised when there is a syntax error in the code.
AssertionError:  Raised when an assertion statement fails.
SystemExit:  Raised by the sys.exit() function to exit the program.
OverflowError:   Raised when the result of an arithmetic operation is too large to be represented by the number's type.
MemoryError:   Raised when an operation runs out of memory.
ModuleNotFoundError:   Raised when a module cannot be found.
NotImplementedError:   Raised when an abstract method is not implemented in a subclass.
OverflowError:   Raised when a calculation exceeds the maximum limit for a numeric type.
RecursionError:  Raised when the maximum recursion depth has been exceeded.
TabError:   Raised when inconsistent use of tabs and spaces in indentation is detected.
UnicodeError:  Raised when there is an error decoding or encoding a Unicode string.
'''