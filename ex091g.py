from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
ranking = list(sorted(jogo.items(), key=itemgetter(1), reverse=True))
print('-=' * 30)
print(f'{'== RANKING DOS JOGADORES ==':^29}')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
