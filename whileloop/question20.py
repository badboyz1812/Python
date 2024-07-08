#Program to enter the numbers till the user enters 0. And count the number of positive and negative number,

count = 0 #This variable is intialized to count the number of positive number entered by the user.
count1 = 0 #This variable is intialized to count the number of negative numbers entered by the user.

x = int(input("Enter the value: ")) #x is variable which contains the value entered by the user.

while(x!=0): #while loop is used to check the value entered by the user is not equal to 0.
    if(x>=1): #if loop is used to check whether the value entered by the user is greater than 1.
        count +=1 #if true, the count variable is incremented.
        x= int(input("Enter the value: ")) #futher it asks the user to enter the value for the variable x.
    else: #if condition is false, it enters into the else part.
        count1 +=1 # increments the variable name count1.
        x = int(input("Enter the value: ")) #futher it asks the user to enter the value for the variable x.

else:
    print("The count of positive numbers",count)
    print("The count of negative number",count1)
