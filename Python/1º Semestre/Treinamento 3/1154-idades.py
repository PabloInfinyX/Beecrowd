Idade = int(input())
Anos = Idade
Quantidade = 1

while Idade >= 1:
    Idade = int(input())
    if Idade >= 1:
        Anos = Anos + Idade
        Quantidade = Quantidade +1
else:
    Media = Anos / Quantidade
    print(f'{Media:.2f}')