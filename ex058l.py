from random import randint
tentativas = 1
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.''')
computador = randint(0, 10)
palpite = int(input('Qual é o seu palpite? '))
while palpite != computador:
    if palpite < computador:
        print('Mais... Tente mais uma vez.')
    elif palpite > computador:
        print('Menos... Tente mais uma vez.')
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
