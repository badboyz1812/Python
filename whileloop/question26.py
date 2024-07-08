#Program to accept ten numbers from the user and find the average.

i =0
sum =0
while(i<10):
    num = int(input("Enter a number: "))
    sum += num
    avg = sum/10
    i += 1

print(f"The sum of the number {sum} and the average is {avg}")