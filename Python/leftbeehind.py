# Using Python 3
# https://open.kattis.com/problems/leftbeehind



sweet, sour = map(int, input().split())
answer = []

while(sweet or sour):
    if(sweet + sour == 13):
        answer.append("Never speak again.")
    elif(sweet == sour):
        answer.append("Undecided.")
    elif(sweet > sour):
        answer.append("To the convention.")
    elif(sweet < sour):
        answer.append("Left beehind.")

    sweet, sour = map(int, input().split())

for a in answer: print(a)
