Divida = int(input())
Parcelas = int(input())
count = 1

while Divida > 0:
    if Divida - Parcelas > -1:
        print(f'pagamento: {count}')
        print(f'antes = {Divida}')
        print(f'depois = {Divida-Parcelas}')
        print(f'-----')
        Divida = Divida - Parcelas
        count += 1
    else:
        if Divida > 0:
            print(f'pagamento: {count}')
            print(f'antes = {Divida}')
            Divida = 0
            print(f'depois = 0')
            print(f'-----')
