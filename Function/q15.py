#Python function to accept a hypen-separated sequence of words as input and prints the words in a hypen-separated sequence after sorting them alphabetically.

items = [n for n in input().split('-')]

items.sort()

print('-'.join(items))