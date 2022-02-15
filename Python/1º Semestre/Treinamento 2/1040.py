Notas = input()
N1, N2, N3, N4 = Notas.split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
Media = (2 * N1 + 3 * N2 + 4 * N3 + N4) / 10
format(Media, '.2f')
if Media >= 7.0:
    print(f'Media: {Media:.1f}')
    print('Aluno aprovado.')
elif Media <= 4.9:
    print(f'Media: {Media:.1f}')
    print('Aluno reprovado.')
elif Media >= 5.0 and Media <= 6.9:
    N5 = float(input())
    print(f'Media: {Media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {N5:.1f}')
    Mediafinal = (N5 + Media) / 2
    if Mediafinal >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {Mediafinal:.1f}')
    elif Mediafinal <= 4.9:
        print(f'Aluno reprovado.')
        print(f'Media final: {Mediafinal:.1f}')
