def open_file(filename):
    encoding = input("Input the encoding for the file(ASCII,UTF-16,UTF-8) ")
    try:
        with open(filename,'r',encoding=encoding) as file:
            contents = file.read()
            print("The contents of the file: ")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issuse occured while reading the file.")

filename = input("enter the filename: ")

open_file(filename)