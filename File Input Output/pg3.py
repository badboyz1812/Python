def file_read(filename):
    from itertools import islice
    with open(filename,'w') as f:
        f.write("Python exercise\n")
        f.write("java exercise\n")
    txt = open(filename)
    print(txt.read())

file_read("file.txt")
    