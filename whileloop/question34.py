#program to find the sum of the following series.
#1+8+27.....n terms

n = int(input("Enter the number of terms: "))
sum =0
i = 1
while(i<=n):
    sum = sum + pow(i,3)
    i += 1
print(f"The sum is {sum}")