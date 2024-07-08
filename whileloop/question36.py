#Program to find the sum of the series.
# s = 1+4-9+16-25+36...n terms.

n = int(input("Enter the number of terms: "))
i = 2   
sum = 0 
sum2 = 0
while(i<=n):
    sum = sum + i**i

    sum2 = sum - (i+1)**(i+1)

    i +=1
print(sum)



