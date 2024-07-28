color = ['Red','Blue','Orange','Pink','Black']
with open("file.txt",'w') as f:
    for c in color:
        f.write("%s\n"%c)

content = open("file.txt")
print(content.read())

