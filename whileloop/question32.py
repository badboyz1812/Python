#Program to find the sum of the following series.
#1+x/1!+x^2/2!....x^n/n!

def fact(n):
    f =1
    for i in range(1,n+1):
        f = f*i
    return(f)

sum = 1

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
i=1
while(i<n):
    sum  = sum+x**i/fact(i)
    i += 1
print(sum)
