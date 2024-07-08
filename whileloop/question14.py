#Program to display the number names of a digit entered by the user.

x = input("Enter the number: ")

#store the string in the form of list
li = list(x)

#store the length of the string in variable y
y = len(li)

#initalize a variable i with value zero
i=0

#create a dictionary, where the key contains the number and value contains the name of the digit
n= {0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"}

#Perform while loop operation to print the digits in the form of names.

while(i<y):
    print(n[int(li[i])],end ='')
    i +=1