#Program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.
x = 100
y = 500

while(x<=y):
    if (x%13 == 0 and x%3 != 0 ):
        print(x)
    x += 1