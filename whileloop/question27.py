#program to accept 10 numbers from the user and find the largest and smallest.
i = 0
list=[]
while(i<10):
    num = int(input("Enter the number: "))
    list.append(num)
    i += 1
list.sort()

print(list)
print("The largest number is",list[-1])
print("The smallest number is",list[0])

