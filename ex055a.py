lista = [] # Lista vazia
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    lista += [peso] # Adiciona todos os pesos a lista.
lista.sort() # Sorteia todos os pesos da lista, deixando em ordem crescente.
print(f'O maior peso lido foi de {lista[4]:.1f}Kg')
print(f'O menor peso lido foi de {lista[0]:.1f}Kg')
