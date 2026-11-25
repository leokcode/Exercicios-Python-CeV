print('-=' * 10)
print(f'{'Gerador de PA 2.0':^20}')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro # A variável termo começa com o primeiro termo.
cont = 1 # Aqui ele vai contar quantos termos foram.
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    cont += 1
print('FIM')
