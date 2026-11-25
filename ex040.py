n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
if media >= 7:
    print('O aluno está APROVADO!')
elif media < 5:
    print('O aluno está REPROVADO!')
elif media >=5 and media <7: #Aqui poderia ser usado o else, ou elif 7 < media >= 5:
    print('O aluno está de RECUPERAÇÃO!')
