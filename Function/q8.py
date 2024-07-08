#Python function to print only the unique elements from the list.

def unique_list(l):
    x =[]
    for a in l:
        if a not in x:
            x.append(a)

    return x

print(unique_list([1,1,1,2,2,3,4,5,5,6,7,7]))
                

