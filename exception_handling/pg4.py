def get_value(prompt):
    while True:
        try:
            value =float(input(prompt))
            return value
        except ValueError:
            print("Invalid input.Enter a valid input")


n1 = get_value("Enter the value1: ")
n2 = get_value("Enter the value2: ")
result = n1*n2


print("Product of two number: ",result)