#program to find the sum for the following series.
#x+x^2/2+...x^n/n
sum = 0
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
i = 1
while(i<=n):
    sum = sum + x**i/i
    i +=1
print(sum)