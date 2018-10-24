# Using Python 3
# https://open.kattis.com/problems/ostgotska

str = input()

count = 0
words = str.split(' ')

for w in words:
    count += "ae" in w

if(count/len(words) >= 0.4):
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
