#Python function to create and print a list where values are squares of numbers between 1 to 30

def square():
    list = []
    for i in range(1,31):
        list.append(i*i)
    return list

print(square())