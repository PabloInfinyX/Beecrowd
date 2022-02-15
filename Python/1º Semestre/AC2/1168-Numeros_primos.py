INICIO = int(input())
FIM = int(input())
Primos = 0

for num in range (INICIO, FIM + 1):
    mult = 0
    for count in range(1,num + 1):
        if num % count == 0:
            mult = mult + 1

    if(mult==2):
        print(count)
        Primos = Primos + 1
print(f'primos: {Primos}')
