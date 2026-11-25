números = list()
while True:
    r = ' '
    n = (int(input('Digite um valor: ')))
    if n in números:
        print('Valor duplicado! Eu não vou adicionar...')
    else:
        números.append(n)
        print('Valor adicionado com sucesso...')
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 10)
números.sort()
print(f'Você digitou os valores {números}')
