#Program to find the sum of the sequence.
#1+1/2!+1/3!------1/n!

n  = int(input("Enter the number of terms: "))

sum = 1
i =1
f =1
while(i<=n):
    f = f*i
    sum = sum + 1/f
    i += 1
print(sum)
