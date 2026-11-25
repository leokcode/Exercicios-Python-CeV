from math import radians, cos, sin, tan
ang = float(input('Digite o angulo que você deseja : '))
rad = radians(ang)
se = sin(rad)
co = cos(rad)
ta = tan(rad)
print(f'O ângulo de {rad} tem o SENO de {se:.2f}.')
print(f'O ângulo de {rad} tem o COSSENO de {co:.2f}.')
print(f'O ângulo de {rad} tem a TANGENTE de {ta:.2f}.')
