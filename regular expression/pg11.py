import re
def check(string):
    pattern  = r'\w+\S*$'
    if re.search(pattern,string):
        return "Found a Match!"
    else:
        return "Not a Match!"
    
print(check("The quick brown fox jumps over the lazy dog."))
print(check("The quick brown fox jumps over the lazy dog. "))
print(check("The quick brown fox jumps over the lazy dog "))