num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num = [num1, num2, num3]
num.sort() # Quando usa o .sort() em uma lista, eles são colocados em ordem crescente.
print(f'O menor número foi {num[0]}.')
print(f'O maior número foi {num[2]}.')
