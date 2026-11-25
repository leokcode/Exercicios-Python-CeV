dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prester a começar uma viagem de {dist}Km.')
preço = dist * 0.50 if dist <=200 else dist * 0.45
print(f'E o preço da passagem será de R${preço:.2f}')
