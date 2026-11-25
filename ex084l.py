dados = []
pessoas = []
maior = menor = 0
while True:
    resp = ' '
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if menor > dados[1]:
            menor = dados[1]
        if maior < dados[1]:
            maior = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
