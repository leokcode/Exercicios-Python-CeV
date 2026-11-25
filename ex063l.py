print('-' * 30)
print(f'{'Sequência de Fibonacci':^30}')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 30)
t1 = 0
t2 = 1
count = 3
print(f'{t1} → {t2} → ', end='')
while n >= count:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    count += 1
    t1 = t2
    t2 = t3
print('FIM')
print('~' * 30)
