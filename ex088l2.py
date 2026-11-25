from time import sleep
from random import sample
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=' * 3, 'SORTEANDO', n, 'JOGOS', '-=' * 3)
for c in range(1, (n + 1)):
    ns = sample(range(1, 60), 6)
    ns.sort()
    print(f'Jogo {c}: {ns}')
    sleep(1)
    ns.clear()
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
