from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura') # Esses itens são numerados, começando do zero em diante, dependendo do número de itens dentro da lista.
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')       
if computador == 1: # Computador jogou papel
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

if computador == 2: # Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLiDA')
