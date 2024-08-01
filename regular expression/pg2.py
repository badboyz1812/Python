import re
def check(text):
    pattern  = r'^a(b*)$'
    if re.search(pattern,text):
        return 'Found a match'
    else:
        return 'Not a match!'
    
print(check('abbb'))
print(check(''))
print(check('a'))
        