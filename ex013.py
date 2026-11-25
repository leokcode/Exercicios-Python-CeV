s = float(input('Qual é o salário do funcionário? R$'))
novo = s + (s * 15 / 100)
print(f'Um funcionário que ganhava R${s:.2f}, com 15% de aumento, passa a receber R${novo:.2f}.')
