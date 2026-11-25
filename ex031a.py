dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prester a começar uma viagem de {dist}Km.')
if dist <=200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print(f'E o preço da passagem será de R${preço:.2f}')
