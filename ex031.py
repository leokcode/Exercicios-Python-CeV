dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prester a começar uma viagem de {dist}Km.')
if dist <=200:
    print(f'E o preço da sua passagem será de R${dist * 0.50 :.2f}')
else:
    print(f'E o preço da sua passagem será de R${dist * 0.45 :.2f}')
