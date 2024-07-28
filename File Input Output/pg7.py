def read_file(filename):
    content_array =[]
    with open(filename) as f:
        for line in f:
            content_array.append(line)
        print(content_array)

filename = input("Enter the filename: ")

read_file(filename)