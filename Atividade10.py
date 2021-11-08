import math
x1 = float(input('Valor de x1 = '))
y1 = float(input('Valor de y1 = '))
x2 = float(input('Valor de x2 = '))
y2 = float(input('Valor de y2 = '))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'{distancia:.4f}')
print()