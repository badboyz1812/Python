import re
def check(string):
    pattern  = r'ab?'
    if re.search(pattern,string):
        return "Found a Match!"
    else:
        return "Not a Match!"
    
print(check("abbb"))
print(check("abcc"))
print(check('abcc'))