#Program to find the factorial of a number.

f = int(input("Enter a positive number: "))

def factorial(f):
    fact =1
    for i in range(1,f+1):
        fact = fact*i
    return fact

print(factorial(f))
