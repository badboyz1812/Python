#Program to find armstrong number or not

x = input("Enter the number:") #store in the form of string

#find the length of the string
y = len(x)
#store the value in the form of list
l = list(x)

#intialize a variable with value 0.
i = 0
p = 0
#while loop
while(i<y):
    p = p + int(l[i]) ** 3
    i += 1

#check the value of p is equal to the value provided by the user.

if(int(x) == p):
    print(x,"is a armstrong number")
else:
    print("it is not armstrong number.")    
    