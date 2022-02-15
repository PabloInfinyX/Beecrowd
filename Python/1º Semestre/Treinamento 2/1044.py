#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

ENTRADA = input()
A, B = ENTRADA.split()
A = float(A)
B = float(B)
MULT = B / A 
MULT1 = A / B
if MULT.is_integer() or MULT1.is_integer():
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
