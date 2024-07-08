#Program to find the sum of the series.
#1+2+6+24+120+....nterm.
n = int(input("Enter the number of terms: "))
sum = 0
pr = 1
i = 1
while(i<=n):
    pr = i*pr
    print(pr,end ="+")
    sum += pr
    i += 1
print(" =",sum) 