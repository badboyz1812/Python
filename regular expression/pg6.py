import re
def check(string):
    pattern  = r'abb(b*)'
    if re.search(pattern,string):
        return "Found a match!"
    else:
        return "Not a match!"
    
print(check("abb"))
print(check("abbb"))
print(check("abbbbbc"))