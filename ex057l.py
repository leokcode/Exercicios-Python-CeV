sx = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sx != 'M' and sx != 'F':
    sx = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
if sx == 'M':
    sx = 'Masculino'
if sx == 'F':
    sx = 'Feminino'
print(f'Sexo {sx} registrado com sucesso.')
