print('-=' * 10)
print(f'{'Gerador de PA v2.0':^20}')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
count = 1
termo = primeiro
while count <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    count += 1
print('FIM')
