#Você gosta de jogos? Silvio gosta! Ainda mais de jogos matemáticos e que precisam de raciocínio lógico. Como Silvio é muito criativo, criou um jogo para passar o tempo com seus amigos entre os intervalos das aulas. O jogo é simples, um de seus amigos diz em voz alta um número natural maior ou igual a dois e Silvio deve dizer rapidamente o número ímpar anterior e o par posterior ao número pronunciado.
#Você é um programador que gosta de desafios, afinal todo programador encara desafios o tempo todo, e por isso se ofereceu para criar um programa para automatizar a resposta de Silvio, recebendo como entrada um número natural maior ou igual a dois e exibindo o ímpar anterior e o par posterior.

X = int(input())
Y = int()
while X < 2:
    X = int(input())
for num in range(X - 2, X):
    if num % 2 != 0:
        impar = num
for num in range(X + 1, X + 3):
    if num % 2 == 0:
        par = num
print(f'{impar} {par}')
