#Python function to check whether the number is perfect number or not.

def perfect_num(n):
    sum = 0
    for i  in range(1,n):
        if n % i ==0:
            sum += i

    return sum==n

print(perfect_num(6))

