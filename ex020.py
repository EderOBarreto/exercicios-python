from random import shuffle

aluno1 = input('Nome do aluno 1:')
aluno2 = input('Nome do aluno 2:')
aluno3 = input('Nome do aluno 3:')
aluno4 = input('Nome do aluno 4:')

alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(alunos)

print('Primeiro {}\nSegundo {}\nTerceiro {}\nQuarto {}'.
      format(alunos[0], alunos[1],
             alunos[2], alunos[3]))
