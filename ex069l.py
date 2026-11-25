homens = mais18 = mulheresmenos20 = 0
while True:
    sexo = continuar = ' '
    print('-' * 25)
    print(f'{'CADASTRE UMA PESSOA':^25}')
    print('-' * 25)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    if continuar == 'N':
        break
print('-' * 25)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos.')
