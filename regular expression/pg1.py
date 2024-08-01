import re
def check(string):
    str1 = re.compile(r'[^a-zA-Z0-9]')
    string = str1.search(string)
    return not bool(string)


print(check("AbcDIGDews19203"))
print(check("$#%!acmdsknfsij"))
print(check("*&%@#!}{"))
