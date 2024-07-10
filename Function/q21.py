#Python program that invokes a function after a specific period of time.

from time import sleep
import math

def delay(fn,ms,*args):
    sleep(ms/1000)
    return fn(*args)

print("Sqrt after a specific milliseconds:")

print(delay(lambda x:math.sqrt(x),100,16))
print(delay(lambda x:math.sqrt(x),1000,200))
print(delay(lambda x:math.sqrt(x),2000,245600))