#Program to convert a binary to decimal number.

bin = input("Enter a binary number: ") #contains the binary number entered by the user.
dec = 0 #intialize decimal as 0.
p = 0 #intialize place as 0.
for i in reversed(bin):   #perform for loop by using reverse method of bin.
    dec =dec + int(i)* pow(2,p) #To find decimal value.
    p +=1 #increment the value of p.
print(f"decimal number of binary value {bin} is the number {dec}")