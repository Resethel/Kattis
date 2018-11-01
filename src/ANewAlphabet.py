# Using Python 3
# https://open.kattis.com/problems/anewalphabet


dict = {
    'a':"@",
    'b':"8",
    'c':"(",
    'd':"|)",
    'e':"3",
    'f':"#",
    'g':"6",
    'h':"[-]",
    'i':"|",
    'j':"_|",
    'k':"|<",
    'l':"1",
    'm':"[]\/[]",
    'n':"[]\[]",
    'o':"0",
    'p':"|D",
    'q':"(,)",
    'r':"|Z",
    's':"$",
    't':"']['",
    'u':"|_|",
    'v':"\/",
    'w':"\/\/",
    'x':"}{",
    'y':"`/",
    'z':"2"
}



sentence = input().lower()

for c in sentence:
    if(c in dict):
        print(dict[c], end ='')
    else:
        print(c, end = '')
print()
