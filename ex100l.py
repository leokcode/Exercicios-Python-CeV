from random import randint
from time import sleep


def sorteia(num):
    print(f'Sorteando {len(num)} valores da lista ', end='')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapares(num):
    spar = 0
    for n in num:
        if n % 2 == 0:
            spar += n
    print(f'Somando os valores pares de {números}, temos {spar}')


números = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
sorteia(números)
somapares(números)
