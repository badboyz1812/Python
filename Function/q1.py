#Python function to find the maximum of three number.

x =int(input("Enter a value: "))
y = int(input("Enter a value: "))
z =int(input("Enter a value: "))


def max(x,y,z):
    if(x>y and x>z):
        print(f"{x} is the largest number.")
    elif(y>x and y>z):
        print(f"{y} is the largest number.")
    else:
        print(f"{z} is the largest number")

max(x,y,z)
