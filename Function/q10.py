#Python function to print even numbers of the list.


def even_number(list):
    x =[]
    for a in list:
        if a%2 == 0:
            x.append(a)

    return x
          

list = [1,2,3,4,5,6,7,8,9]
print(even_number(list))

        