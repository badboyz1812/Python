#Program to add the number until the user enters the number.

choice  = 'Y' #initalize a variable name choice whose value is a string
sum = 0       #intialixze a variable name sum whose value is sum
while choice.upper() == 'Y': #using of upper function is used as user can enter lowercase of y.
    x = int(input("Enter the value:"))
    sum  = sum + x   #Perform addition with pervious value and current value.
    choice  = input("Enter the choice(Y/N)?:") #This is used to chose the user whether he can continue.


print("sum of the number is",sum)    #print statement to provide when user exit from the operation.
