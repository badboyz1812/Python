import re
def check(string):
    pattern = r'[A-Z]+[a-z]+$'
    if re.search(pattern,string):
        return "Found a Match!"
    else:
        return "Not Matched"
    
print(check("AaBbGg"))
print(check("Python"))
print(check("python"))
print(check("PYTHON"))
print(check("aA"))
print(check("Aa"))