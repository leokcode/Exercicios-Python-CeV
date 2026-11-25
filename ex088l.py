from time import sleep
from random import randint
num = []
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=' * 3, 'SORTEANDO', n, 'JOGOS', '-=' * 3)
for c in range(1, (n + 1)):
    while len(num) < 6:
        a = randint(1, 60)
        if a not in num:
            num.append(a)
    num.sort()
    print(f'Jogo {c}: {num}')
    sleep(1)
    num.clear()
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
