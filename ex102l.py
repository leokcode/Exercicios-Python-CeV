def fatorial(n, show=False):
    '''-> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n. '''
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f


n = int(input('Digite um número para calcular seu fatorial: '))
print('-' * 30)
print(fatorial(n, show=False))
#help(fatorial)
