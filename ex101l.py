from datetime import date
def voto():
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade >= 18 and idade < 65:
        print('VOTO OBRIGATÓRIO!')
    elif idade >= 16 and idade <= 17 or idade >= 65:
        print('VOTO OPCIONAL!')
    elif idade > 0 and idade < 16:
        print('NÃO VOTA!')
        
    
print('-' * 30)
nasc = 0
while nasc <= 0:
    nasc = int(input('Em que ano você nasceu? '))
voto()
