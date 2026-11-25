from cores import *

def leiaint(msg):
    valor = 0
    while True:
        try:
            n = int(input(msg))
            return n
        except (TypeError, ValueError):
            print(f'{cor(1)}ERRO! Digite um número inteiro válido.{cor(0)}')
        except (KeyboardInterrupt):
            print(f'{cor(1)}Usuário preferiu não digitar esse número!{cor(0)}')
            return 0


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU')
    c = 1
    for item in lista:
        print(f'{cor(3)}{c}{cor(0)} - {cor(6)}{item}{cor(0)}')
        c += 1
    print(linha())
    opc = leiaint(f'{cor(3)}Sua Opção: {cor(0)}')
    return opc
