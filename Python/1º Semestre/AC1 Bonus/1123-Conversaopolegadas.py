#Megan quer comprar um novíssimo smartphone e está muito empolgada com as possibilidades que uma tela de tantas polegadas pode oferecer para seu entretenimento. Mas há um problema, Megan percebeu que não sabe lidar com polegadas, afinal sempre realizou cálculos usando centímetros e gostaria de se basear nessa unidade de medida para imaginar o tamanho de tela que comprará. Você pode ajudar Megan?
#Seu trabalho é construir um programa que receba como entrada um número real, simbolizando uma quantidade de polegadas, e exiba o equivalente em centímetros. Lembre-se que uma polegada equivale a 2,54 cm.

Polegadas = float(input())
Centimetros = Polegadas * 2.54
print(f'{Centimetros:.3f}')
