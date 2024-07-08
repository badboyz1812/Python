#Program to find the product of the digit entered by the user
x = int(input("Enter a number: "))
r =0
p = 1
while(x != 0):
    r = x%10
    p *= r
    x = x//10
print(f"product is {p}")


