def open_file(filename):
    try:
        with open(filename,'w') as file:
            contents = file.read()
            print("File contents")
            print(contents)
    except :
        print("Error: Permission denied to open the file")

filename = input("Enter the filename ")
open_file(filename)