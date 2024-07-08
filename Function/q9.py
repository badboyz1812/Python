#Python function that takes number as parameter and checks the number is prime or not.

def prime(n):
    k =0
    if (n == 0 or n==1):
        print(f"{n} is not a prime number ")
    else:
        i = 2
        while(i<n):
            if(n%i == 0):
                k += 1
            i += 1
    if k == 0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

n = int(input("Enter a number "))
prime(n)
    
