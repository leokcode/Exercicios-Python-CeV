nome = list()
notas = list()
alunos = list()
mostrar = 500
while True:
    resp = ' '
    nome.append(str(input('Nome: ')).strip().title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nome.append(notas[:])
    alunos.append(nome[:])
    notas.clear()
    nome.clear()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'N°','NOME','      MÉDIA')
print('-' * 20)
for i, d in enumerate(alunos):
     print(f'{i:<3}{d[0]:<10}{(d[1][0] + d[1][1]) / 2:>6}')
print('-' * 60)
while True:
    while mostrar > (len(alunos) - 1) and mostrar != 999:
        mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        for i, d in enumerate(alunos):
            if mostrar == i:
                print(f'Notas de {d[0]} são {d[1]}')
                print('-' * 60)
                mostrar = 500
    if mostrar == 999:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

