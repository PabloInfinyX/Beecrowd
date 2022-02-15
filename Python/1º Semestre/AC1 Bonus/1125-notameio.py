Trabalho = float(input())
Prova = float(input())
Media = (Trabalho + Prova) / 2
if Media >= 6:
    print(f'aprovado')
elif Media < 6:
    if ((Trabalho + 10) / 2) >= 6:
        print(f'talvez com a sub')
    else:
        print(f'reprovado')
