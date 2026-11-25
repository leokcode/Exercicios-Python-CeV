from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif 14 >= idade > 9:
    print('Classificação: INFANTIL')
elif 19 >= idade > 14:
    print('Classificação: JUNIOR')
elif 25 >= idade > 19:
    print('Classificação: SENIOR')
elif idade > 25:
    print('Classificação: MASTER')
