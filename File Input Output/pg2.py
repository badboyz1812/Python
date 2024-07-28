def file_read(filename,nlines):
    from itertools import islice
    with open(filename) as f:
        for line in islice(f, nlines):
            print(line)

print(file_read("file.txt",3))