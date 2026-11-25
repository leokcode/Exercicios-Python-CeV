print('-=' * 10)
print(f'{'Gerador de PA v3.0':^20}')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
count = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while count <= total:
        print(f'{termo} → ', end='')
        count += 1
        termo += razão
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')