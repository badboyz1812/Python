#Python program to multiply all the number in the list.

num = [1,2,3,8,-9,-10]

def mul(n):
    i = 0
    mult = 1
    for i in n:
        mult = mult * i
    return mult

print(mul(num))