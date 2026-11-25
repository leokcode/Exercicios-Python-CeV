sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # O [0] é pra pegar só a primeira letra do que foi digitado.
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')
