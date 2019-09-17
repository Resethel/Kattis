# Using Python 3
# https://open.kattis.com/problems/runlengthencodingrun

str = input()
_output = ""
count = 0
last = str[2]

if(str[0] == 'E'):
    for i in range(2, len(str)):
        if(str[i] != last):
            print(last, end = '')
            print(count, end = '')
            count = 1
            last = str[i]
        else:
            count += 1
    print(last, end = '')
    print(count)

elif(str[0] == 'D'):
    for i in range(2, len(str)):
        if(not(i % 2)):
            last = str[i]
        else:
            for a in range(int(str[i])):
                print(last, end = '');
    print()
