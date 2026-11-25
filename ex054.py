from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em qual ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    elif idade < 18:
        totmenor += 1
    if totmaior == 1:
        maior = 'pessoa maior'
    else:
        maior = 'pessoas maiores'
    if totmenor == 1:
        menor = 'pessoa menor'
    else:
        menor = 'pessoas menores'
print(f'Ao todo tivemos {totmaior} {maior} de idade.')
print(f'E também tivemos {totmenor} {menor} de idade.')
