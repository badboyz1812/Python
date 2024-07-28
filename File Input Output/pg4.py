import sys
import os

def file_read_(fname,lines):
    bufsize =8192 #the size of buffer to read at a time,initially set to 8192 bytes.

    #os.stat is used to return the status of the file such as filesize,creation time and updating and more.
    fsize =os.stat(fname).st_size 
    #counter to keep track of number of iteration.
    iter = 0

    with open(fname) as f:
        if bufsize>fsize:
            bufsize = fsize-1
            data =[]
            while True:
                iter +=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data)>=lines or f.tell() == 0:
                    print("".join(data[-lines:]))
                    break


file_read_("file.txt",2)

