#Program to find the factorial for the number given bythe user.

x  = int(input("Enter the number for the factorial:"))

f = 1
i = 1
while(i <= x):
    f = f * i
    i = i + 1
    print(f)
          