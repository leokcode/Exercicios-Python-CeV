from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 se não tem): '))
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contratação'] - nasc) + 35
print('-=' * 30)
for k, v in dados.items():
    if k == 'Salário':
        print(f'  - {k} tem o valor R${v:.2f}')
    else:
        print(f'  - {k} tem o valor {v}')
