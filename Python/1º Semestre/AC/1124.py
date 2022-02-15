X = int(input())
Y = int()
while X < 2:
    X = int(input())
for num in range(X - 2, X):
    if num % 2 != 0:
        impar = num
for num in range(X + 1, X + 3):
    if num % 2 == 0:
        par = num
print(f'{impar} {par}')
