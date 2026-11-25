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
    count = i
    if i < f:
        while count <= f:
            print(f'{count} ', end='', flush=True)
            count += p
            sleep(0.25)
        print('FIM!')
        lin()
    else:
        while count >= f:
            print(f'{count} ', end='', flush=True)
            count -= p
            sleep(0.25)
        print('FIM!')
        lin()


lin()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
