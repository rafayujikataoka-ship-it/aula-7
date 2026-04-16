meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun','jul', 'ago', 'set', 'out', 'nov', 'dez']

soma = 0
for i in range(12):
    salario = float(input(f' Digite o salário de {meses[i]}: '))
    soma += salario

salario13 = soma/12
ferias = salario13 * 1/3
print (f' 13 salário {salario13}, ferias {ferias}')

