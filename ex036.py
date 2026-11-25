casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento: '))
calc = casa / (financiamento * 12)
if financiamento == 1:
    year = 'ano'
else:
    year = 'anos'
print(f'Para pagar uma casa de R${casa:.2f} em {financiamento} {year}, a prestação será de R${calc:.2f}')
if calc <= salário * (30 / 100):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
