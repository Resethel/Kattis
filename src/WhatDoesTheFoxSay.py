# Using Python 3
# https://open.kattis.com/problems/whatdoesthefoxsay

n = int(input())

out = [""] * n

for i in range(n):
    known = []
    sounds = [x for x in input().split(' ')]

    str = input()
    while(str != "what does the fox say?"):
        known.append(str.split(' ')[-1])
        str = input()

    for s in sounds:
        if(not(s in known)):
            out[i] += s + " "
    out[i] = out[i][:-1]


for output in out: print(output)
