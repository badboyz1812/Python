#Program to find the factors of a number using a loop.

x = int(input("Enter a number: "))

i = 1
while(i<=x):
    if(x%i==0):
        print(i)
    i += 1
