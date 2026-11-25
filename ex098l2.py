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
            sleep(0.25)
            count += p
        print('FIM!')
        lin()
    if i > f:
        while count >= f:
            print(f'{count} ', end='', flush=True)
            sleep(0.25)
            count -= p
        print('FIM!')
        lin()


lin()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
lin()
contador(ini, fim, pas)
