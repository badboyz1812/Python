def div(x,y):
    try:
        result =x/y
        print("The result is ",result)
    except ZeroDivisionError:
        print("The division of zero operation is not allowed")

x = int(input("Enter a value1: "))
y = int(input("Enter a value2: "))


div(x,y)
