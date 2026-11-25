a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < (c + b) and b < (a + c) and c < (a + b):  
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!') #Todos os lados iguais.
    elif a != b != c != a:
        print('ESCALENO!') # Todos os lados diferentes.
    elif a == b != c or a != b == c or a == c != b: # Aqui poderia ser usado o else:
        print('ISÓSCELES!') # Apenas 2 lados iguais.
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
