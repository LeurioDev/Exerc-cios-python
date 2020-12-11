import random
n1 = str(input('Digite o nome do 1ª aluno: '))
n2 = (input('Digite o nome do 2ª aluno: '))
n3 = str(input('Digite o nome do 3ª aluno: '))
n4 = str(input('Digite o nome do 4ª aluno: '))
s = str(random.choice([n1, n2, n3, n4]))
print('O sorteado é a/o :{}'.format(s))