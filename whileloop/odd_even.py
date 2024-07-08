a = int(input("Enter the number: "))
if(a != 0 and a % 2 == 0):
    print(a,"is a even number")
elif(a != 0 and a % 2 == 1):
    print(a,"is a odd number")  
else:
    print(a,"is a invalid")