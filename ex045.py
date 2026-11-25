from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
computador = randint(0 , 2)
jogador = int(input('Qual é a sua jogada? '))
if computador == 0:
    computador = 'PEDRA'
elif computador == 1:
    computador = 'PAPEL'
elif computador == 2:
    computador = 'TESOURA'
if jogador == 0:
    jogador = 'PEDRA'
elif jogador == 1:
    jogador = 'PAPEL'
elif jogador == 2:
    jogador = 'TESOURA'
else:
    print('Jogada inválida, tente novamente!')
    jogador = 'jogada inválida'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*12)
print(f'Computador jogou {computador}!')
print(f'Jogador jogou {jogador}!')
print('-='*12)
if jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
    print('JOGADOR VENCEU!')
elif computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
    print('COMPUTADOR VENCEU!')
elif jogador == computador:
    print('EMPATE')
