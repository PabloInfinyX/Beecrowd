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
