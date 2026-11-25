def notas(*n, sit=False):
    '''=> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não mostrar a situação.
    :return: dicionário com várias informações sobre a situação da turma.. '''
    tot = mai = men = med = 0
    for i, v in enumerate(n):
        if i == 0:
            mai = men = v
            tot += v
        else:
            if mai < v:
                mai = v
            if men > v:
                men = v
            tot += v
    med = tot / len(n)
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = mai
    dic['Menor'] = men
    dic['Média'] = med
    if sit:
        if med < 5:
            dic['Situação'] = 'RUIM'
        if med >= 5 and med < 7:
            dic['Situação'] = 'RAZOÁVEL'
        if med >= 7:
            dic['Situação'] = 'BOA'
    return dic


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
#help(notas)
