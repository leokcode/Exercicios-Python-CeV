lista = []
print('-=' * 30)
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=' * 30)
print(f'Você digitou os valores {lista}')
print(f'O menor valor digitado foi {min(lista)} nas posições ', end='' )
for p, l in enumerate(lista):
    if l == min(lista):
        print(f'{p}... ', end='')
print()
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for p, l in enumerate(lista):
    if l == max(lista):
        print(f'{p}... ', end='')
print()
print('-=' * 30)
