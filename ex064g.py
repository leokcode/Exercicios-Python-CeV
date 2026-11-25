n = count = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Voce digitou {count} números e a soma entre eles foi {soma}.')
