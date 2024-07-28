def file_read(filename):
    file = open(filename)
    contents = file.readlines()
    print(contents)


filename = input("Enter the filename: ")

file_read(filename)