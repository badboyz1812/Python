#Python function to print number of local variables.

def count():
    x =20
    y =34
    str1 ="ram"
    str2 = "rock"
    

print(count.__code__.co_nlocals)