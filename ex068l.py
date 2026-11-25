from random import randint
count = 0
print('=-' * 15)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
while True:
    tipo = ' '
    print('=-' * 15)
    jogador = int(input('Diga um número: '))
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    total = jogador + computador
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            count +=1
        else: 
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            count +=1
        else:
            break
    print('Vamos jogar novamente...')
print('VOCÊ PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {count} vezes.')
