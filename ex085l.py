números = [[], []]
for v in range(1, 8):
    núm = int(input(f'Digite o {v}° valor: '))
    if núm % 2 == 0:
        números[0].append(núm)
    else:
        números[1].append(núm)
números[0].sort()
números[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {números[0]}')
print(f'Os valores ímpares digitados foram: {números[1]}')