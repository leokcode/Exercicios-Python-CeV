n =  int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ',end='')
for count in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    c -= 1
    f *= count
print(f'{f}')
