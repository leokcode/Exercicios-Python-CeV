from datetime import date
aatual = date.today().year
anasc = int(input('Ano de nascimento: '))
idade = aatual - anasc
falta = 18 - idade
passou = idade - 18
aalist = anasc + 18
print(f'Quem nasceu em {anasc} tem {idade} anos em {aatual}.')
if idade < 18:
    print(f'Ainda faltam {falta} anos para o alistamento.')
    print(f'Seu alistamento será feito em {aalist}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {passou} anos.')
    print(f'Seu alistamento foi em {aalist}.')
