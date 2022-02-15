#Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
#O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

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