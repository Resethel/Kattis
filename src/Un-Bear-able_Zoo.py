# Using Python 3
# https://open.kattis.com/problems/zoo

def getZoo(n):
    zoo = {}
    names = []

    for i in range(n):

        buff = input().split()
        animal = buff[-1].lower()

        if animal not in zoo:
            names.append(animal)
            zoo[animal] = 1
        else:
            zoo[animal] += 1

        names.sort()
        zoolist = []

        for name in names:
            zoolist.append(f"{name} | {zoo[name]}")

    return zoolist

################################################################################

N = int(input())
output = []
count = 0
while(N != 0):
    count += 1
    output.append(f"List {count}:")
    output += getZoo(N)
    N = int(input())

for text in output:
    print(text)
