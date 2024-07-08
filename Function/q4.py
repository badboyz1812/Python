#Program to reverse a string.
string = input("Enter a string: ")

def rev(str):
    i = len(str)
    rstr = ''
    while i > 0:
        rstr +=str[i-1]
        i -= 1
    return rstr

print(rev(string))
