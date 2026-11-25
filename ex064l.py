n = 0
count = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        count += 1
        soma += n
print(f'Voce digitou {count} números e a soma entre eles foi {soma}.')
