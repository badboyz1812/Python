#program to find HCF entered by the user

x = int(input("Enter the number1: "))
y = int(input("Enter the number2: "))

#assign reminder value as 1.
rem = 1

#if condition
if x>y:
    while rem!=0:
        rem = x%y
        if rem == 0:
            hcf = y
        else:
            x = y
            y = rem
else:
    while  rem!=0:
        rem = y%x
        if rem == 0:
            hcf = x
        else:
            y = x 
            x =rem
print("HCF of two number",hcf)                   