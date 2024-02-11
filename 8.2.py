
x = input()
if len(x) > 1000:
    print('false')
else:
    while "  " in x:
        x = x.replace("  ", " ")
    
print(x)

    