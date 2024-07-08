#Program to find the sum of digits given by the user

x = int(input("Enter a number: "))
sum = 0
r = 0
while(x != 0):
    r = x%10
    sum += r
    x = x//10
print(f"sum is {sum}")        
