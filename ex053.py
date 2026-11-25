frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
frase = frase.replace('À', 'A').replace('Á', 'A').replace('Â', 'A').replace('Ã', 'A')
frase = frase.replace('È', 'E').replace('É', 'E').replace('Ê', 'E')
frase = frase.replace('Ì', 'I').replace('Í', 'I').replace('Î', 'I')
frase = frase.replace('Ò', 'O').replace('Ó', 'O').replace('Ô', 'O').replace('Õ', 'O')
frase = frase.replace('Ù', 'U').replace('Ú', 'U').replace('Û', 'U')
inversão = frase[::-1] # O -1 faz a frase ser lida de trás pra frente.
print(f'O inverso de {frase} é {inversão}.')
if frase == inversão:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
