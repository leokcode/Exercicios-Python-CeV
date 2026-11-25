dados = dict()
lista = list()
totidade = média = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    totidade += dados['idade']
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        média = totidade / len(lista)    
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for d in lista:
    if d['sexo'] in 'F':
        print(f'{d["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > média:
        for k, v in p.items():
            if k in 'idade':
                print(f'{k} = {v}:')
            elif k in 'nome':
                print(f'    {k} = {v}; ', end='')
            else:
                print(f'{k} = {v}; ', end='')
