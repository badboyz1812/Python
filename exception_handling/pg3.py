def open_file(filename):
    try:
        file = open(filename,'r')
        contents = file.read()
        print("File contents")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("File not found")


filename = input("Enter the file name ")

open_file(filename)