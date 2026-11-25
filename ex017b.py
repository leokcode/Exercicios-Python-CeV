from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = sqrt((co * co) + (ca * ca))
print(f'A hipotenusa vai medir {h:.2f}.')
