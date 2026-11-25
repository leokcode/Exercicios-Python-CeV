def área(larg, comp):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


print('-' * 30)
print(f'{'Controle de Terrenos':^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
