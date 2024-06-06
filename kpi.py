nome = input('Digite seu nome: ')
salario = float(input('Digite o seu salário: '))
valor_bonus = float(input('Digite o valor do bônus: '))

kpi = (1000 + salario) * valor_bonus
print(f'Olá {nome}, o seu valor bônus foi de {valor_bonus}')
