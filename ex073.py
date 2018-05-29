placar = ('Flamengo','Fluminense','Atlético', 'São Paulo', 'Grêmio',
          'Corinthians','Palmeiras','Internacional','Sport Recife',
          'Cruzeiro','América-MG','Botafogo','Vasco da Gama','EC Vitória',
          'Bahia','Santos','Atlético-PR','Chapecoense','Ceará SC', 'Paraná')

print('Primeiros colocados:')
for t in placar[:5]:
    print(t)

print('\nÚltimos colocados:')
for t in placar[-4:]:
    print(t)

print('\nOrdem alfabética:')
for pos, t in enumerate(sorted(placar)):
    print(f'{pos+1:02}   {t}')

print('\nO Chapecoense  está {0}º posição.'.format(placar.index('Chapecoense') + 1))
