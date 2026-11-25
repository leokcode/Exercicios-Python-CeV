times = ('Flamengo', 'Palmeiras', 'Juventude', 'Vasco', 'Fluminense',
         'Internacional', 'Fortaleza', 'Ceará SC', 'Corinthians', 'Botafogo',
         'Bragantino', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo',
         'Mirassol', 'Atlético-MG', 'Santos', 'EC Vitória', 'Sport Recife')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Mirassol está na {times.index('Mirassol') + 1}ª posição ')
print('-=' * 15)
