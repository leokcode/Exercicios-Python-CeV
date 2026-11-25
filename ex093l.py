dados = {}
dados['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
gols = []
tot = 0
part = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
for c in range(1, (part + 1)):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols'] = gols
    tot += gols[-1]
dados['total'] = tot
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {part} partidas.')
for p in range(1, (part + 1)):
    print(f'    => Na partida {p}, fez {dados["gols"][p - 1]} gols.')
print(f'Foi um total de {tot} gols.')
