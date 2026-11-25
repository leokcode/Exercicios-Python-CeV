def cor(cor=0):
    cores = (   '\033[m',     # 0 Sem cor
                '\033[031m',  # 1 Vermelho
                '\033[0;32m', # 2 Verde
                '\033[0;33m', # 3 Amarelo
                '\033[0;34m', # 4 Roxo
                '\033[0;35m', # 5 Rosa
                '\033[0;36m') # 6 Azul
    return cores[cor]
