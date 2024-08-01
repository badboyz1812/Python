import re
def check(string):
    pattern = r'[a]+[A-Za-z]*[b]$'
    if re.search(pattern,string):
        return 'Found a Match!'
    else:
        return 'Not a Match'
    
print(check("aabbbbd"))
print(check("aabAbbbc"))
print(check("accddbbjjjb"))