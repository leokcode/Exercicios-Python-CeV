soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # Serve para contar quantos números tem dentro do rage. Sem a simplificação ficaria count = count + c
        soma += c # Soma todos os números dentro do range. Sem a simplificação ficaria soma = soma + c
print(f'A soma de {cont} valores solicitados é {soma}')
