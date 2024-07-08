#program to check whether the number is prime or not 
x = int(input("Enter the number: "))
k = 0
if(x == 0 or x ==1):
    print(f"{x} is not a prime number") 
else:
    i=2
    while(i<x):
        if(x%i == 0):
            k += 1
        i += 1 
if k == 0:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")               
        
        


