def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    

def leiadinheiro(msg=""):
    while True:
        valor = 0
        n = (input(msg)).replace(',', '.').strip()
        if is_float(n):
            valor = float(n)
            return valor
        else:
            print(f'\033[0;31mERRO: "{n}" é um preço inválido.\033[m')
