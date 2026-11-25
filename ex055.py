lista = [] # Lista vazia
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    lista += [peso] # Adiciona todos os pesos a lista.
print(f'O maior peso lido foi de {max(lista):.1f}Kg')
print(f'O menor peso lido foi de {min(lista):.1f}Kg')
