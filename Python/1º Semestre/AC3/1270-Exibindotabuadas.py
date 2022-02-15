A = int(input())
B = int(input())
if A <= B:
    for t in range(A, B+1):
        for multiplicador in range(1,10+1):
            print(f'{t} x {multiplicador} = {t * multiplicador}')
            if multiplicador == 10:
                print('----------')
else:
    print('Nenhuma tabuada no intervalo!')