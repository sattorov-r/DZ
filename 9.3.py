s = input().split()
s2 = []
for i in s:
    if i in s2:
        print('YES')
    else:
        print('NO')
    s2.append(i)        