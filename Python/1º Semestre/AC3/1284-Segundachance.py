Alunos = int(input())
nota_aluno = []
nota_atividade = []
nota_final = []
veralterada = []
notas_alteradas = 0

for prova in range(Alunos):
    nota_aluno.append(float(input()))
for atividade in range(Alunos):
    nota_atividade.append(float(input()))

for notas in range (Alunos):
    if nota_atividade[notas] == 10.0:
        nota_atividade[notas] = 2
    else:
        nota_atividade[notas] = 0

for final in range(Alunos):
    if nota_aluno[final] == 10:
        nota_final.append(10.0)
        veralterada.append('-')
    if nota_aluno[final] <= 8:
        nota_final.append(nota_aluno[final] + nota_atividade[final])
        if nota_aluno[final] != nota_final[final]:
            notas_alteradas += 1
            veralterada.append('*')
        else:
            veralterada.append('-')
    if nota_aluno[final] > 8 and nota_aluno[final] < 10:
        if nota_atividade[final] == 2:
            nota_final.append(10.0)
            notas_alteradas += 1
            veralterada.append('*')

print(f'NOTAS ALTERADAS: {notas_alteradas}')
for x in range(Alunos):
    print(f'{veralterada[x]}(00{x+1}) original: {nota_aluno[x]:05.2f} | final: {nota_final[x]:05.2f}')