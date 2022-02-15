Doacao = float(input())
Total = 0
while Doacao != -1.0:
    Total += Doacao
    Doacao = float(input())

RS = Total * 2.50

print(f'VC$ {Total:.2f}')
print(f'R$ {RS:.2f}')
