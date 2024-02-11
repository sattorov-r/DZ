x = int(input('Введите натуральное число до 2 млрд: '))
if x > 2e9:
    print("false")
else:    
    n = 1
    j = 0
    while n <= x:
        if x % n == 0:
            j += 1
            n += 1
        else: n += 1
    print('Количество натуральных делителей: ', j)    
