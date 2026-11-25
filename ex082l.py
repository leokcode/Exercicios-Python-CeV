lista = []
listapar = []
listaímpar = []
while True:
    resp = ' '
    n = lista.append(int(input('Digite um valor: ')))
    if lista[-1] % 2 == 0:
        listapar.append(lista[-1])
    else:
        listaímpar.append(lista[-1])
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaímpar}')
