def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço, aum, red):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'{'Preço analisado:':<20}{moeda(preço)}')
    print(f'{'Dobro do preço:':<20}{moeda(preço * 2)}')
    print(f'{'Metade do preço:':<20}{moeda(preço / 2)}')
    print(f'{aum}{'% de aumento:':<18}{moeda(preço + (preço * aum / 100))}')
    print(f'{red}{'% de redução:':<18}{moeda(preço - (preço * red / 100))}')
    print('-' * 30)
