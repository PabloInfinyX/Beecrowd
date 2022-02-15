#Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

N = int(input())

for num in range(1, N + 1):
    if num % 2 == 0:
        print(f'{num}^2 =', num ** 2)