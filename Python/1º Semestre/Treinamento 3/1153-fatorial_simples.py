#Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

N = int(input())
Fator = N - 1

while N > 13:
    N = int(input())

while Fator > 1:
    N = N * Fator
    Fator = Fator -1

print(N)