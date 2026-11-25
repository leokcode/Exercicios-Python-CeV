def metade(preço=0, fmt=False):
    res = preço / 2
    if fmt:
        return moeda(res)
    else:
        return res
    

def dobro(preço=0, fmt=False):
    res = preço * 2
    if fmt:
        return moeda(res)
    else:
        return res
    

def aumentar(preço=0, taxa=0, fmt=False):
    res = preço + (preço * taxa / 100)
    if fmt:
        return moeda(res)
    else:
        return res


def diminuir(preço=0, taxa=0, fmt=False):
    res = preço - (preço * taxa / 100)
    if fmt:
        return moeda(res)
    else:
        return res
    

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
