tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;32m', end='') # Cor para os números divisíveis.
        tot += 1 # Contagem do total de números divisíveis.
    else:
        print('\033[31m', end='') # cor para os números não divisíveis.
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes.') # O \n foi para o print descer pra linha de baixo e o \33 foi para voltar para a cor padrão.
if tot == 2: # Se o número for dividido por 2 números, ele é primo.
    print('E por isso ele é PRIMO!')
else: # Se não, ele não é primo.
    print('E por isso ele NÃO É PRIMO!')
