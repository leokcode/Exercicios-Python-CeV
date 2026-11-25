soma = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        count += 1
        soma += num
        if count == 1:
            par = 'número par'
        else:
            par = 'números pares'
print(f'Você informou {count} {par}, e a soma deles foi {soma} ')
