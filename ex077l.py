palavras = ('aprender','programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro' )
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for palavra in p.lower():
        if palavra in 'aááâãeéèêiíìîoóòôõuúùû':
            print(f'{palavra} ', end='')
