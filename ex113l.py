def leiaint(msg):
    valor = 0
    while True:
        try:
            n = int(input(msg))
            return n
        except (TypeError, ValueError):
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuário preferiu não digitar esse número!\033[m')
            return 0


def leiafloat(msg):
    valor = 0
    while True:
        try:
            f = float(input(msg))
            return f
        except (TypeError, ValueError):
            print(f'\033[0;31mERRO! Digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuário preferiu não digitar esse número!\033[m')
            return 0


print('-' * 30)
n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n} e o número real digitado foi {f}')
