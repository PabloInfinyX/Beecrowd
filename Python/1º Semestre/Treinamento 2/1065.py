VALOR1 = int(input())
VALOR2 = int(input())
VALOR3 = int(input())
VALOR4 = int(input())
VALOR5 = int(input())
PARES = 0
if VALOR1 % 2 == 0:
    PARES = PARES + 1
if VALOR2 % 2 == 0:
    PARES = PARES + 1
if VALOR3 % 2 == 0:
    PARES = PARES + 1
if VALOR4 % 2 == 0:
    PARES = PARES + 1
if VALOR5 % 2 == 0:
    PARES = PARES + 1
print(f'{PARES} valores pares')
