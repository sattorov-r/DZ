s1 = input().split()
s2 = input().split()
if len(s1) > 100000 or len(s2) > 100000:
    print('false')
else:
    m1 = set(s1)
    m2 = set(s2)
    m3 =m1.intersection(m2)
print(len(m3))