salário = int(input('Degite o salário: '))
aumento = (salário*15)/100
print('Salário Antigo: ${:.2f}\nSalário com aumento de 15%: ${:.2f}'.format(salário,salário+aumento))