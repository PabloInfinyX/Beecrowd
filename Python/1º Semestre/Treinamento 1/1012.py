ENTRADA = input()
A, B, C = ENTRADA.split()
A = float(A)
B = float(B)
C = float(C)
TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * C ** 2
TRAPEZIO = ((A + B) / 2) * C
QUADRADO = B ** 2
RETANGULO = A * B
print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')
