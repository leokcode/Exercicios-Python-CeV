from random import randint
números = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO menor valor foi {min(números)}')
print(f'O maior valor foi {max(números)}')
