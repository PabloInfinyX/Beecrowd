#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, 
# o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

codpeca1, numpeca1, valorpeca1 = [float(i) for i in input().split(' ')]
codpeca2, numpeca2, valorpeca2 = [float(i) for i in input().split(' ')]

total = (numpeca1 * valorpeca1) + (numpeca2 * valorpeca2)

print(f'VALOR A PAGAR: R$ {total:.2f}')
