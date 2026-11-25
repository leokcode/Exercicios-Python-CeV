matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares =  maior = terceiracoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            terceiracoluna += matriz[l][c]
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
print('-=' * 30)    
print(f'A soma dos valores pares é igual a {somapares}.')
print(f'A soma dos valores da terceira coluna é igual a {terceiracoluna}.')
for n in matriz[1]:
    if n == 0:
        maior = n
    else:
        if maior < n:
            maior = n
print(f'O maior valor da segunda linha é {maior}.')
