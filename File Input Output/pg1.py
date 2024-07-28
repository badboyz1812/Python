def read_file(filename):
    file = open(filename)
    contents = file.read()
    print(contents)

filename = input("Enter the filename: ")

read_file(filename)
