import re
def check(string):
    pattern = r'^[a-z]+_[a-z]+$'
    if re.search(pattern,string):
        return 'Match Found!'
    else:
        return 'Not a Match'
    
string = input("Enter a string: ")
print(check(string))