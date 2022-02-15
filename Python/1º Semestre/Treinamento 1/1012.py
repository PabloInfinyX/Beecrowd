#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

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
