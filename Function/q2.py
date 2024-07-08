#Python function to sum all the values in the list.
 
list = (8,9,-1,10)

def sum(l):
    i=0
    sum =0
    for i in l:
        sum = sum + i
        
    print(sum)

sum(list)