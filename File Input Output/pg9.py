def file_length(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
        return i+1
    

filename = input("Enter the filename: ")

print("Number of lines in the file: ",file_length(filename))