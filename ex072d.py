cont = ('zero' , 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resp = ' '
    núm = int(input('Digite um número entre 0 e 20: '))
    if núm > 20 or núm < 0:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {cont[núm]}')
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('=' * 30)
    if resp == 'N':
        break
print(f'{'FIM DO PROGRAMA':=^30}')
print('=' * 30)
