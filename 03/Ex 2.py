#Calcula a distância entre 2 pontos

import math

x1 = int(input("Coordenada x1 de P1: "))
y1 = int(input("Coordenada y1 de P1: "))
x2 = int(input("Coordenada de x2 de P2: "))
y2 = int(input("Coordenada de y2 de P2: "))

d = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
print("Distância entre P1 e P2 é: ", d)