# Using Python 3
# https://open.kattis.com/problems/fbiuniversal

from math import pow

dict = {
    'B' : '8',
    'G' : 'C',
    'I' : '1',
    'O' : '0',
    'Q' : '0',
    'S' : '5',
    'U' : 'V',
    'Y' : 'V',
    'Z' : '2'
}

ref = "0123456789ACDEFHJKLMNPRTVWX"

n = int(input())
outputs = []
for i in range(n):
    _str = [x for x in input().split()][1]

    # Replacing confusing characters
    for j in range(len(_str)):
        if(_str[j] in dict):
            _str[j] = dict[_str[j]]

    # Checking the last digit
    checkDigit = ( 2  * ref.index(_str[0])  + 4  * ref.index(_str[1]) + 5  * ref.index(_str[2]) \
                 + 7  * ref.index(_str[3])  + 8  * ref.index(_str[4]) + 10 * ref.index(_str[5]) \
                 + 11 * ref.index(_str[6])  + 13 * ref.index(_str[7])) % 27

    if( ref[checkDigit] != _str[-1]):
        out = str(i+1) + " Invalid"
    else:
        _str = _str[:-1]
        sum = 0
        length = len(_str)
        for l in range(length):
            sum += ref.index(_str[l]) * pow(27,(length-1) - l)
        out = str(i+1) + " " + str(sum)[:-2] #[:-2] to remove the trailling '.0'

    outputs.append(out)

for o in outputs: print(o)
