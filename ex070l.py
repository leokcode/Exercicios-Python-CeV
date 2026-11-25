print('-' * 35)
print(f'{'LOJA SUPER BARATÃO':^35}')
print('-' * 35)
total = maisde1k = maisbaratopreço = count = 0
maisbaratonome = ' '
while True:
    continuar = ' '
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preço = int(input('Preço: R$'))
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 35)
    count += 1
    total += preço
    if preço > 1000:
        maisde1k += 1
    if count == 1:
        maisbaratopreço = preço
        maisbaratonome = produto
    else:    
        if preço < maisbaratopreço:
            maisbaratopreço = preço
            maisbaratonome = produto
    if continuar == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^35}')
print('-' * 35)
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {maisde1k} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbaratonome} que custa R${maisbaratopreço:.2f}')
