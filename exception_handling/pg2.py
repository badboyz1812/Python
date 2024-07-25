def value(prompt):
    try:
        x = int(input(prompt))
        return x
    except ValueError:
        print("Invalid input type")



n = value("Input ")
print("Input",n)

