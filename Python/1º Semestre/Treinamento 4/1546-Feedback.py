#Muitos alunos de diversas universidades conhecem o portal de programação IRU. Este portal possui milhares de problemas de programação disponíveis. 
#Diariamente a equipe do IRU recebe diversos feedbacks (elogios, bugs, dúvidas, sugestões, ...) que precisam primeiramente ser atribuídos para membros da equipe resolver.
#Como a equipe é muito ocupada e não tem tempo para classificar estes feedbacks
#você foi convidado a escrever um programa que faça isso e mostre quem será o membro responsável por resolver e responder o feedback.
#Os membros responsáveis em cada setor são:
#Elogios: Rolien
#Bugs: Naej
#Dúvidas: Elehcim
#Sugestões: Odranoel

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