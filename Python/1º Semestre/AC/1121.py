Valor = float(input())
Quantidade = int(input())
Valorquant = Valor * Quantidade
Valorquant = float(Valorquant)
Desconto = Quantidade + 10
Descontototal = (Valorquant * Desconto) / 100
Valortotal = Valorquant - Descontototal
print(f'{Valorquant:.2f}')
print(f'{Valortotal:.2f}')
