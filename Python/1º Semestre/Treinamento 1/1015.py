#Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, 
#mostrando 4 casas decimais após a vírgula, segundo a fórmula:
#fórmula no link: https://www.beecrowd.com.br/judge/pt/problems/view/1015

A = input()
B = input()
X1, Y1 = A.split()
X2, Y2 = B.split()
X1 = float(X1)
X2 = float(X2)
Y1 = float(Y1)
Y2 = float(Y2)
DISTANCIA = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 0.5
print(f'{DISTANCIA:.4f}')
