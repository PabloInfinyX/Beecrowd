#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. 
#A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

A = int(input())
B = int(input())
C = float(input())
SALARY = C * B
print(f'NUMBER = {A}')
print(f'SALARY = U$ {SALARY:.2f}')
