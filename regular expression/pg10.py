import re
def check(string):
    pattern = r'^\w+'
    if re.search(pattern,string):
        return "Found a match"
    else:
        return "Not a match"
    

print(check("The quick brown fox jumps over the lazy dog."))
print(check(" The quick brown fox jumps over the lazy dog."))