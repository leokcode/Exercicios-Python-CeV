def lin():
    print('-' * 30)


lin()
print(f'{'Controle de Terrenos':^30}')
lin()
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))


def area():
    s = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {s}m².')


area()
