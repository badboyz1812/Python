mycode = 'print("Hello world")'

code = """
def multiply(x,y):
    return x*y

print('multiply of 2 and 3 is: ',multiply(2,3))

"""

exec(mycode)
exec(code)
