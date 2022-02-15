Lista = []

n = 3

for num in range(0, n):
    Valor = int(input())
    if Valor >= 1:
        Lista.append(Valor)
      
Maior = max(Lista)
Posicao = Lista.index(Maior)
print(Maior)
print(Posicao + 1)
