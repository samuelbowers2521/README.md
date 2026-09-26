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
from pygame import init

import fibp # pyright: ignore[reportMissingImports]
import sys
sys.path.append('/uts/guido/lib/python')
import fibo, sys  # pyright: ignore[reportMissingImports]
dir(fibo)
['__name__', 'fib', 'fib2']
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
a = [1, 2, 3, 4, 5]
import fibo  # pyright: ignore[reportMissingImports]
fibo = fibo.bib
dir()
import sound.effect.echo # pyright: ignore[reportMissingImports]
sound.effect.echofilter(input, output, delay=0.7, atten=4) # pyright: ignore[reportUndefinedVariable]
from sound.effect import echo # pyright: ignore[reportMissingImports]
from sound.effect.echo import echofilter  # pyright: ignore[reportMissingImports]
echofilter(input, output, delay=0.7, atten=4) # pyright: ignore[reportUndefinedVariable]
__all__ = [
    "echo", # refers to the 'echo.py' file
    "surround", # refers to the 'surround.py' file
    'reverse', # !!! refers to the 'reverse' function now !!!
]
def reverse(msg: str): # <-- this name shadows 'reverse.py' submodule
    return msg[::-1]  #     im the case of a 'from sound.effects import *'
import sound.effects.echo # pyright: ignore[reportMissingImports]
import sound.effects.surround # pyright: ignore[reportMissingImports]
from sound.effects import * # pyright: ignore[reportMissingImports]
from . import echo # pyright: ignore[reportMissingImports]
from .. import formates # pyright: ignore[reportMissingImports]
from ..filters import equalizer # pyright: ignore[reportMissingImports]
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
'Results of the 2016 Referendum'
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes 
s = 'Hello, world'
str(s)
'Hello world.'
repr(s)
"'Hello world.'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) and y is repr(y) 
print(s)
# The repr() of a string adds string add string quotes and backLashes:
hello = 'hello, world\n'
hello = repr(hello)
print(hellos) # pyright: ignore[reportUndefinedVariable]
'hello, world\n'
# THe argument to repr() may be any python object:
repr((x, y, ('spam)', 'eggs')))
import math 
print('f The value of pi is approximately {math.pi:.3f}.')
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
    # We can check that the file has been automatically closed.
    import sys
    f = open('myfile.txt')
    s = f.readline()
    i = init('s.strip')()
    def this_falis():
        x = 1/0
        this_falis
        def bool_return():
            return True
bool_return() # pyright: ignore[reportUndefinedVariable]
False
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
x = MyClass
def __init__(self):
    self.data = []
x = MyClass()
