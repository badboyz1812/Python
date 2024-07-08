#program to display the sum of odd numbers and even numbers separately that fall between two numbers entered by user.
even = 0
odd = 0
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
while(x>y):
    y = int(input("Enter the second number: "))

while(x<=y):
    if(x%2 == 0):
        print(x,"is a even number")
        even += x
    else:
        print(x,"is a odd number")
        odd += x
    x += 1

else:
    print(f"sum of even number is {even}")       
    print(f"sum of odd number is {odd}")

