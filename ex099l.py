from time import sleep
def maior(*num):
    print('Analisando os valores passados...')
    sleep(1)
    mai = 0
    for i, n in enumerate(num):
        print(n, end=' ', flush=True)
        sleep(0.5)
        if i == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}')
    print('-=' * 20)


print('-=' * 20)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
