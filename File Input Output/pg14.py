with open("file.txt") as f,open("file1.txt") as f1:
    for line1,line2 in zip(f,f1):
        print(line1+line2)
        