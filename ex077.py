palavras = ('palavra', 'batata', 'errado', 'certo', 'bug',
            'nao sei', 'chato', 'legal', 'lento', 'rapido',
            'compartilhe', 'inscreva se', 'cancado', 'acho',
            'que', 'ja', 'e', 'o', 'suficiente')
vogais = ('a', 'e', 'i', 'o', 'u')
resul = '';
"""
for p in palavras:
    for v in vogais:
        resul += p.count(v) * f'{v} '
    print(f'Na palavra {p.upper()} temos {resul}')
    resul = ''
"""

for p in palavras:
    for l in p:
        resul += ''.join([v + ' ' for v in vogais if l == v ])
    print(f'Na palavra {p.upper()} temos {resul}')
    resul = ''


