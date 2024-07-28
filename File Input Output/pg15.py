import random
def random_file(filename):
    lines  = open(filename).read().splitlines()
    return random.choice(lines)

filename = input("Enter the filename: ")

print(random_file(filename))