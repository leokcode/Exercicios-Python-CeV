def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: ')).strip().capitalize()
g = str(input('Número de Gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
print('-' * 30)
if n in ' ':
    ficha(gol=g)
else:
    ficha(n, g)
