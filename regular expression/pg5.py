import re
def check(string):
    pattern = r'ab{3}+'
    if re.search(pattern,string):
        return "found a match!"
    else:
        return "Not a Match!"
    
print(check("aaaabbbbbbc"))
print(check("ab"))
print(check("abaa"))