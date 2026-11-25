lista = []
ex = lista.append(str(input('Digite a expressão: ')).strip())
aberto = fechado = 0
for p in lista:
    for palavra in p:
        if palavra == '(':
            aberto += 1
        elif palavra == ')':
            fechado += 1
if aberto == fechado:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
