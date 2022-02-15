qtd_canais = int(input()) #quantos canais
dados = []

for i in range(qtd_canais):
    inputdados = input().split(';') #separar informações por ';'
    dados.append(inputdados) #dados recebe o input
    dados[i][1] = int(dados[i][1]) #transformar 2º dado em int
    dados[i][2] = float(dados[i][2]) #transformar 3º dado em float

bonus1 = float(input())
bonus2 = float(input())

for bonus in range(qtd_canais): 
    if dados[bonus][1] >= 1000: #se tiver mais de 1.000 inscritos
        dados[bonus].append(dados[bonus][1]//1000) #adicionar valor de bonus
    else:
        dados[bonus].append(0) #zerar bonus

print('''-----
BÔNUS
-----''')

for z in range(qtd_canais):
    if dados[z][3] == 'sim':
        print(f'{dados[z][0]}: R$ {dados[z][2] + (dados[z][4]*bonus1):.02f}')
    else:
        print(f'{dados[z][0]}: R$ {dados[z][2] + (dados[z][4]*bonus2):.02f}')
