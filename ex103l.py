def ficha(n, g=0):
    if n in ' ':
        n = '<desconhecido>'
    if gols.isalpha():
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip().capitalize()
gols = str(input('Número de Gols: ')).strip()
print('-' * 30)
ficha(nome, gols)
