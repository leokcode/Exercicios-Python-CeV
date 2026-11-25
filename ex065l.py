continuar = 'S'
count = soma = maior = menor = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    count += 1
    soma += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Você digitou {count} números e a média foi {soma / count}')
print(f'O maior valor foi de {maior} e o menor foi de {menor}')
