from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opção = 0
while opção != 7:
    print('''      [ 1 ] SOMAR
      [ 2 ] SUBTRAIR
      [ 3 ] MULTIPLICAR
      [ 4 ] DIVIDIR
      [ 5 ] MAIOR NÚMERO
      [ 6 ] NOVOS NÚMEROS
      [ 7 ] SAIR''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {v1} + {v2} é {v1 + v2}')
    elif opção == 2:
        print(f'A subtração entre {v1} - {v2} é {v1 - v2}')
    elif opção == 3:
        print(f'A multiplicação entre {v1} x {v2} é {v1 * v2}')
    elif opção == 4:
        print(f'A divisão entre {v1} / {v2} é {v1 / v2}')
    elif opção == 5:
        if v1 > v2:
            maior = v1
        else:
            maior = v2

        print(f'Entre {v1} e {v2} o maior valor é {maior}')
    elif opção == 6:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 7:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')
