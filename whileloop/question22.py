#program to convert a number to binary format.
num = int(input("Enter a number: "))
bin = 0 #binary is intialized to 0, to hold the binary value 0 or 1.
p = 1  #p is intailized to 1 to set the place of the digits in(ones,tens,hundreds etc)
n = num #intializing of n with num value
while n>0:  #perform while operation until n is greater than 0.
    rem = n%2      #find the reminder of the value.
    bin = bin + rem*p #placing the binary value 
    p = p*10            #increasing the place holder.
    n = n//2             #performing integer division.

print(f"binary number of {num} is {bin}")
