# Using Python 3
# https://open.kattis.com/problems/sok

juices = list(map(float, input().split(' ')))
recipe = list(map(float, input().split(' ')))

ratio = []
for i in range(len(recipe)):
    ratio.append(juices[i]/recipe[i])

min_ratio = min(ratio)

leftOver = []
for j in range(len(juices)):
    leftOver.append(juices[j] - recipe[j] * min_ratio)

print(format(leftOver[0], '.6f'), end = ' ')
print(format(leftOver[1], '.6f'), end = ' ')
print(format(leftOver[2], '.6f'))
