import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def clean(file):
    cleaned = ['']
    for line in file:
        cleaned.append(line.strip())
    return cleaned

f1 = clean(read_file(file1))
f2 = clean(read_file(file2))

list_difference = [item for item in f1 if item not in f2]

print(list_difference)
