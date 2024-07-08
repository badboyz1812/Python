#Program to count the number of uppercase and lowercase in a string.

str = input("Enter a string: ")
d={"UC":0,"LC":0}
def count(str):
    for i in str:
        if i.isupper():
            d["UC"] += 1
        elif i.islower():
            d["LC"] += 1
        else:
            pass
    print(str)
    print('No of uppercase:',d['UC'])
    print('No of lowercase:',d["LC"])

count(str)
