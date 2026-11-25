print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)
pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = (pt + (10 - 1) * razão) + razão # Formula do décimo termo.
for c in range(pt, décimo, razão):
    print(c, '→', end=' ')
print('Acabou!')
