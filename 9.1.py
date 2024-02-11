n = int(input('Введите число N: '))
y = set()
if (n < 1) or (n > 10000):
    print('N от 0 до 10000!')
else:
    print('Введите', n, 'чисел' )
    x = map(int, input().split())
    for i in x:
        if i > (2*10e9):
            print('false')  
        else:
            y.add(i)
print('Резyльтат: ', len(y))            