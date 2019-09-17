# Using Python 3
# https://open.kattis.com/problems/different

contents = []
numbers = []

while True:
    try:
        l = [int(x) for x in input().split(' ')]
    except EOFError:
        break
    contents.append(l)

for dif in contents:
    print(abs(dif[0] - dif[1]))
