rows, cols = [int(i) for i in input().split()]
table = [input() for i in rows]
word = input()
part = ''
for el in table:
    if word in el:
        print('YES')
        break
    index = 0
    for i in el:
        if i in 
