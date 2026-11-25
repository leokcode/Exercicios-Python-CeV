countp = 0
somaidade = 0
maioridadehomem = 0
nomevelho = '' # Por ser uma string, em vez de zero se utiliza das aspas sem nada.
countf20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    countp += 1
    if p == 1 and sexo == 'M':
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        countf20 += 1
media = somaidade / countp
print(f'A média de idade do grupo é de {media} anos.')
if sexo == 'M':
    print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
if sexo == 'F':
    print(f'Ao todo são {countf20} mulheres com menos de 20 anos.')
