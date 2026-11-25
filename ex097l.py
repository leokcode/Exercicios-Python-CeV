def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'{msg:^{t}}')
    print('~' * t)



escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
