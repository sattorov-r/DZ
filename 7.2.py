n = int(input('Введите число N: '))
x = []
if (n < 1) or (n > 100000):
    print('false')
else:
    print('Введите', n, 'чисел')
    i = map(int, input().split())
    for ai in i:
        if (ai > 10e9) or (ai < 1):
            print('false')
        else:
            x.append(ai)         
x.insert(0, x[-1])
x.pop(-1)
print(x)
