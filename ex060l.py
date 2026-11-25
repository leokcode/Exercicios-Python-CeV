n = int(input('''Digite um número para 
calcular seu Fatorial: '''))
c = n # c de contador, e o contador vai começar com o 'n', no caso o número digitado pelo usuário. 
f = 1 # Fator nulo da multiplicação é 1.
print(f'Calculando !{n} = ', end='')
while c > 0:
    print(f'{c}' , end ='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c # Aqui poderia ser f = f * c
    c -= 1 # Aqui poderia ser c = c - 1, que no caso vai tirar 1 do c.
print(f'{f}')
