X = int(input())
Y = int(input())
Soma = 0
for num in range(X + 1, Y):
    if num % 2 != 0:
        Soma = Soma + num
for num in range(Y + 1, X):
    if num % 2 != 0:
        Soma = Soma + num
print(Soma)