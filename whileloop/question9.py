#Print all the even numbers exclusive both the values enterd by the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number greater than first: "))
while(x>=y):
    print("Invalid")
    y = int(input("Enter the second number: "))

#for excluding
x +=1
y -= 1

#check for even and print
while(x<=y):
    if(x%2 == 0):
        print(x)
        x += 1
    else:
        x += 1    


