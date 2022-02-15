Lista = []

N = int(input()) #Definir quantos dias

for i in range(N):
    K = int(input()) #Definir quantos casos
    for i in range(K):
        Pessoa = int(input())
        if Pessoa == 1: 
            Lista.append('Rolien') 
        elif Pessoa == 2: 
            Lista.append('Naej')
        elif Pessoa == 3: 
            Lista.append('Elehcim')
        else: 
            Lista.append('Odranoel')

print(*Lista, sep='\n')