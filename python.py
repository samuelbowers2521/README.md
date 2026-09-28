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
