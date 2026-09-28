the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
from enum import Enum
from re import match
class Color(Enum = 1):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    color =(input("Enter your choice of 'red', 'blue' or 'green:'"))
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# Now call the function we just defined:
fib(2000)
fib(0)
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result