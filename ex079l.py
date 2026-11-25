listanum = []
while True:
    resp = ' '
    num = (int(input('Digite um valor: ')))
    if num in listanum:
        print('Valor duplicado! Eu não vou adicionar...')
    else:
        listanum.append(num)
        print('Valor adicionado com sucesso...')
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 10)
listanum.sort()
print(f'Você digitou os valores {listanum}')
