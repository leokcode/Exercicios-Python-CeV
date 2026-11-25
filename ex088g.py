from random import randint
from time import sleep
lista = []
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu jogue? '))
for c in range(1, (quant + 1)):
    while len(lista) < 6:    
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        lista.sort()
    print(f'Jogo {c}: {lista}')
    sleep(1)
    lista.clear()
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
