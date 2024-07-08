#Program to print only the odd number from the list l =[23,45,32,25,46,33,71,90].

list  = [23,45,32,25,46,33,71,90]
length = len(list)
i = 0
while(i<length):
    x =int(list[i])
    if(x%2 == 1):
        print(f"{x} is a odd number")
    i += 1