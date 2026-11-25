print('=' * 30)
print(f'{'BANCO CEV':^30}')
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
while True:
    c50 = valor // 50
    r50 = valor % 50
    c20 = r50 // 20
    r20 = r50 % 20
    c10 = r20 // 10
    r10 = r50 % 10
    c1 = r10 // 1
    if c1 == r10:
        break
print('=' * 30)
if c50 > 0:
    print(f'Total de {c50:.0f} cédulas de R$50,00')
if c20 > 0:
    print(f'Total de {c20:.0f} células de R$20,00')
if c10 > 0:
    print(f'Total de {c10:.0f} células de R$10,00')
if c1 > 0:
    print(f'Total de {c1:.0f} células de R$1,00')
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
