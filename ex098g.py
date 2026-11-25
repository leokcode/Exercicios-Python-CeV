from time import sleep
def lin():
    print('-=' * 20)
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
            sleep(0.25)
        print('FIM!')
        lin()
    else:
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.25)
        print('FIM!')
        lin()


# Programa principal
lin()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
