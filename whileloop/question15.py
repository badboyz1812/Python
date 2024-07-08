#Program to print the fibonacci series till n terms using while loop
n = int(input("Enter the fibonacci term: "))

if n == 1: #print the value if the input is 1.
    print("1")
elif n == 2: #print the value if the input is 2.
    print("1 1")
elif n<=1: #print if the value is less than 1
    print("Enter the number greater than 1")    
else:
    ft = 1 #intialize the value of first term
    st = 1 #intialize the value of second term
    print(ft,end=" ")
    print(st,end=" ")
    i = 2   
    while(i<n): #if i value is less than n
        nt = ft + st  # store new term value with first term and second term
        print(nt,end =" ")
        ft = st  #store the value of second term with first term
        st = nt  #store the value of new term with second term
        i +=1  #increment the value of i

