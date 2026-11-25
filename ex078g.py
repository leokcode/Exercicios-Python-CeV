listan = []
maior = 0
menor = 0
print('-=' * 30)
for c in range(0, 5):
    listan.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listan[c]
    else:
        if listan[c] > maior:
            maior = listan[c]
        if listan[c] < menor:
            menor = listan[c]
print('-=' * 30)
print(f'Você digitou os valores {listan}')
print(f'O menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(listan): # i de index, v de valor
    if v == menor:
        print(f'{i}... ', end='')
print()
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(listan):  # i de index, v de valor
    if v == maior:
        print(f'{i}... ', end='')
print()
print('-=' * 30)
