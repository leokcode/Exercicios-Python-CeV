nome = str(input('Digite seu nome completo: ')).strip().title().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[-1]}.') # O valor menos 1 significa o último item da lista.
