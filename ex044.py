print(f'{' LOJAS KLEN ':=^40}')
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é sua opção? '))
if opção == 1:
    valor = compras - (compras * 10 / 100)
elif opção == 2:
    valor = compras - (compras * 5 / 100)
elif opção == 3:
    valor = compras
    print(f'Sua compra será parcelada em 2x de R${valor / 2:.2f} SEM JUROS.')
elif opção == 4:
    parcelas = int(input('Quantas parcelas: '))
    valor = compras + (compras * 20 / 100)
    print(f'Sua compra será parcelada em {parcelas}x de R${valor / parcelas:.2f} COM JUROS.')
if opção == 1 or opção == 2 or opção == 3 or opção == 4:
    print(f'Sua compra de R${compras:.2f} vai custar R${valor:.2f} no final.')
else: 
    print('Opção inválida de pagamento, tente novamente.')
