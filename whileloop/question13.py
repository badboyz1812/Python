#Program to reverse a number entered by user using while loop

x =int(input("Enter a number:"))

r =0 
rev =0 
while(x!=0):
    r = x%10
    rev = rev *10 + r
    x = x//10
print(f"reverse number is {rev}")    

