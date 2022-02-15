n = int(input())
Repetir = 1
CCO = 0
EPR = 0
Intrusos = 0
while n < 1 or n > 100000:
    n = int(input())

while Repetir == 1:
    for i in range(n):
        Aluno = input()
        if Aluno.isalnum:
            Matricula, Turma = Aluno.split()
            if Turma == 'CCO':
                CCO = CCO + 1
            elif Turma == 'EPR':
                EPR = EPR + 1
            elif Turma != 'CCO' and 'EPR':
                Intrusos = Intrusos + 1
    print(f'EPR: {EPR}')
    print(f'CCO: {CCO}')
    print(f'INTRUSOS: {Intrusos}')