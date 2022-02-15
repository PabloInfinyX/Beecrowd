#Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra.
#Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
#O símbolo ( representa "maior que". Por exemplo:
#[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
#(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

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
