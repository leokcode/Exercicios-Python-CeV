def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')


print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
