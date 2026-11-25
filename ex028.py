from random import randint
from time import sleep
print('-=-' * 17)
print('Vou pensar um número entre 0 e 5. Tente advinhar...')
print('-=-' * 17)
num = int(input('Em que número eu pensei? ')) # Número que o usuário vai digitar.
comp = randint(0 , 5) # Número aleatório entre 0 e 5 que o código vai gerar.
print('PROCESSANDO...')
sleep(2) # Função de delay no código.
if num == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {comp} e não no {num}!')
