## Using python3
## https://open.kattis.com/problems/apaxiaaans

name = input()

last = ''
c = ''

for i in range(len(name)):
    c = name[i]
    if (c != last):
        print(c, end = '')
        last = c
print()
