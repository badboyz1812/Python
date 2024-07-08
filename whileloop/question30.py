#Program to print the series till n terms.
#2,22,222,2222.........n terms

n =int(input("Enter the number of terms: "))
str = '2'
i = 0
while(i<n):
    print(str,end=',')
    str = str + '2'
    i += 1
    