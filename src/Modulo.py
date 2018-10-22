#Using Python 3
# Modulo: https://open.kattis.com/problems/modulo

_ins = []

for i in range(10):
    _ins.append(int(input()))

print(len(set([x % 42 for x in _ins])))
