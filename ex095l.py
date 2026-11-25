dadosdict = dict()
gols = list()
dadoslist = list()
while True:
    dadosdict['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    part = int(input(f'Quantas partidas {dadosdict["nome"]} jogou? '))
    for c in range(1, part + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dadosdict['gols'] = gols[:]
    dadosdict['total'] = sum(dadosdict['gols'])
    dadoslist.append(dadosdict.copy())
    gols.clear()
    dadosdict.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30)
print(f'{'Cod':<4}{'Nome':<15}{'Gols':<15}{'Total':<6}')
print('-' * 40)
for i, v in enumerate(dadoslist):
    print(f' {i + 1:<3}{v["nome"]:<15}{str(v["gols"]):<15}{v["total"]:<6}')
print('-' * 40)
while True:
    while True:
        opc = int(input('Mostrar dados de qual jogador? (999 para parar) ' ))
        if opc > 0 and opc <= len(dadoslist) or opc == 999:
            break
        print(f'ERRO! Não existe jogador com código {opc}!')
    if opc <= len(dadoslist):
        print(f' -- LEVANTAMENTO DO JOGADOR {dadoslist[opc - 1]["nome"]}')
        for i, v in enumerate(dadoslist[opc - 1]['gols']):
            print(f'    No jogo {i + 1} fez {v} gols.')
    if opc == 999:
        break
print('<< VOLTE SEMPRE >>')
