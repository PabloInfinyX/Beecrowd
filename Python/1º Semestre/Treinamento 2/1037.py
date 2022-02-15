VALOR = float(input())
if VALOR >= 0.0 and VALOR <= 25.0:
    VALOR = str('[0,25]')
    print(f'Intervalo {VALOR}')
elif VALOR > 25.0 and VALOR <= 50.0:
    VALOR = str('(25,50]')
    print(f'Intervalo {VALOR}')
elif VALOR > 50.0 and VALOR <= 75.0:
    VALOR = str('(50,75]')
    print(f'Intervalo {VALOR}')
elif VALOR > 75.0 and VALOR <= 100.0:
    VALOR = str('(75,100]')
    print(f'Intervalo {VALOR}')
else:
    print('Fora de intervalo')
