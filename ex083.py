texto1 = '((a+b)'
texto12 = 'A+B('
texto2 = ')A+B(-C'
texto21 = '(A+B))-(C+D'
texto3 = '((A+B)+D)'
textovazio = '(a+b)'
abertos = []
fechados = []
resultado = False

for p, c in enumerate(texto21):
    if c == '(':
        abertos.append(p)
    if c == ')':
        fechados.append(p)

def testa_precedencia(ab, fe):
    for i in range(0, len(ab)):
        if ab[i] > fe[i]:
            return False
    return True

if len(fechados) == len(abertos) == 0:
    resultado = True
elif len(fechados) == len(abertos) and fechados[0] > abertos[0]:
    resultado = testa_precedencia(abertos, fechados)
print('{}'.format('Correto' if resultado else 'Incorreto'))



