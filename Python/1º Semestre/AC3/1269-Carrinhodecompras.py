lista1 = input().split()
nova_lista1 = list(lista1)

produtos = []

for i in nova_lista1:
    produtos.append(int(i))

escolha = []
escolha = input().split()

while escolha[0] != 'encerrar':
    if len(escolha) > 1:
            escolha[1] = int(escolha[1])

    if escolha[0] == 'adicionar':
        produtos.append(escolha[1])

    if escolha[0] == 'remover':
        if escolha[1] in produtos:
            produtos.remove(escolha[1])
        else:
            print(f'código {escolha[1]} não encontrado')

    if escolha[0] == 'exibir':
        produtos.sort()
        print(*produtos)


    escolha.clear()

    escolha = []
    escolha = input().split()


produtos.sort()
print(*produtos)