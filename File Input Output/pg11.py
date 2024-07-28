def file_size(filename):
    import os
    file = os.stat(filename)
    return file.st_size

filename = input("Enter the filename: ")

print("The size of the file: ",file_size(filename))