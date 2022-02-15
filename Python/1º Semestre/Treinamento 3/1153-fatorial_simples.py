N = int(input())
Fator = N - 1

while N > 13:
    N = int(input())

while Fator > 1:
    N = N * Fator
    Fator = Fator -1

print(N)