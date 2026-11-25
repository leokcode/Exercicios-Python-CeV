from random import randint
from time import sleep
jogadores = {}
count = 1
for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)
print('Valores sorteados: ')
sleep(1)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# jogadores = dict(sorted(jogadores.items(), key=lambda item: item[1])) # Bota um dicionário em ordem crescente pelo valor.
# jogadores = dict(sorted(dicionario.items())) # Bota um dicionário em ordem crescente pela key.
jogadores = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True )) # Bota um dicionário em ordem decrescente pelo valor.
print('-=' * 30)
print(f'{'== RANKING DOS JOGADORES ==':^29}')
for k, v in jogadores.items():
    print(f'{count}º lugar: {k} com {v}.')
    count += 1
    sleep(1)
