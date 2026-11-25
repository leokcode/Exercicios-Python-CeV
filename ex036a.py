casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * (30 / 100)
if anos == 1:
    year = 'ano'
else:
    year = 'anos'
print(f'Para pagar uma casa de {casa:.2f} em {anos} {year}, ', end='')
print(f'a prestação será de R${prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
    