# Using Python3
# https://open.kattis.com/problems/compoundwords

contents = []
words = []
out = []

# Getting the lines
while True:
    try:
        l = input().split(' ')
    except EOFError:
        break
    contents.append(l)

# Splitting into words
for line in contents:
    for w in line:
        words += [w]

# Making the compound words
for i in range(len(words)):
    for j in range(len(words)):
        if(i != j):
            out.append(words[i] + words[j])

# Removing duplicates and sorting
out = list(set(out))
out.sort()

# Output
for o in out: print(o)
