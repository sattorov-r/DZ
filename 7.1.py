n = int(input('Введите число N: '))      # число N
i = 1                                    # количество строк/ количество чисел
x = []                                   
if (n < 1) or (n > 10000):
    print('false')
else:     
    while (i <= n):
        x.append(int(input()))
        i +=1 
    x.reverse()
    print(x)
