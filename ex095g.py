time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{'cod':^5} ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k + 1:^5} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = (int(input('Mostrar dados de qual jogador? (999 para parar) ')))
    if busca == 999:
        break
    if busca <= 0 or busca > len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca - 1]["nome"]}:')
        for i, g in enumerate(time[busca - 1]['gols']):
            print(f'No jogo {i + 1} fez {g} gols.')
print('-' * 40)
print('<< VOLTE SEMPRE >>')
