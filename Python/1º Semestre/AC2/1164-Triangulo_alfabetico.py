N = int(input())
Letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
vezes = 1
for num in Letras:
    while vezes <= N:
        print(Letras[vezes-1]*vezes)
        vezes += 1
