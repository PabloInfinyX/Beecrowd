INICIO = int(input())
FIM = int(input())

Anos = []
contador = 0
for num in range (INICIO, FIM + 1):
    if num % 4 == 0 and not num % 100 == 0 or num % 400 == 0:
        Anos.append(num)
        contador += 1

print(Anos,sep='\n')
print(f'bissextos: {contador}')