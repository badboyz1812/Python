a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if(a>=b and a>=c):
    print(a,"is the largest number")
elif(b>=c and b>=a):
    print(b,"is the largest number")
else:
    print(c,"is the largest number")    
    