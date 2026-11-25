from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0 # Como a opção vem depois do "while" tem que ter uma variável opção antes.
sleep (1)
while opção != 7:
    print('''    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Multiplicar
    [ 4 ] Dividir
    [ 5 ] Maior
    [ 6 ] Novos números
    [ 7 ] Sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'A subtração de {n1} - {n2} é {n1 - n2}')
    elif opção == 3:
        print(f'A multiplicação de {n1} x {n2} é {n1 * n2}')
    elif opção == 4:
        print(f'A divisão de {n1} / {n2} é {n1 / n2}')
    elif opção == 5:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
        elif n1 == n2:
            print(f'Os dois valores são iguais.')
    elif opção == 6:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 7:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
 