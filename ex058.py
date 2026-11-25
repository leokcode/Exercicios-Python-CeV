from random import randint
palpites = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')
palpite = int(input('Qual é o seu palpite? '))
computador = randint(0, 10)
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
        
print(f'Acertou com {palpites} tentativas. Parabéns!')
