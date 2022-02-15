#Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

X = int(input())
while X < 1 or X > 1000:
    X = int(input())
for num in range(1, X + 1):
    if num % 2 != 0:
        print(num, end = "\n")
