#Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

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