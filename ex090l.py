dados = {}
dados['nome'] = str(input('Nome: ')).strip().title()
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] < 5:
    sit = 'Reprovado'
elif 7 > dados['média'] >= 5:
    sit = 'Recuperação'
elif dados['média'] >= 7:
    sit = 'Aprovado'
dados['situação'] = sit
print('-=' * 30)
for k, v in dados.items():
        print(f'  -{k.title()} é igual a {v}')
        