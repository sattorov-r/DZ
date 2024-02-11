i = 1 
x = []
m = int(input('ГрузоподЬемность лодки: '))
if (m < 1) or (m > 10e6):
    print('Не должна превышать 10e6')
else:
    n = int(input('Количестыо рыбаков: '))
    if (n < 1) or (n > 100):
        print('Не менее 1 и более 100')
    else:
        
        while i <= n:
            print('Вес рыбака: ')
            x.append(int(input()))
            i += 1
        k = sum(x) / m
        if (sum(x) % m) == 0:
            print('Необходимое количество лодок: ', k)
        else:
            k = (sum(x) // m) + 1
            print('Необходимое количество лодок: ', k)