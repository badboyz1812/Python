import re
def check(string):
    pattern = r'^a(b+)?'
    if re.search(pattern,string):
        return 'Found a match!'
    else:
        return "Not a match!"
    

print(check("a"))
print(check("abb"))
print(check('abbca'))