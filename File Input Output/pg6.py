def read_file(filename):
    with open(filename,'r') as f:
        file = f.readlines()
        print(file)


filename =input("Enter the filename: ")

read_file(filename)