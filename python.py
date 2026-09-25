from gzip import WRITE
from http.client import _DataType
from typing import Any

from requests import post


the_world_is_flate = True 
if the_world_is_flate:
    print("Be carefull not to fall off!")
text = "# This is not a comment because it's inside quotes."
      # Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
