#Program to print the following series till n terms.
#1,4,9.....n

n = int(input("Enter the n term: "))
i = 1
while(i<=n):
    m = pow(i,2)
    print(m,end =",")
    i += 1