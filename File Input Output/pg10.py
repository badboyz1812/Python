from collections import Counter
def file_count(filename):
    with open(filename) as f:
        return Counter(f.read().split())
    

filename = input("Enter the filename: ")

print("The count of words in the file: ",file_count(filename))