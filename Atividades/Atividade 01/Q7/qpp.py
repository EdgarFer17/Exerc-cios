'''Uma empresa deseja que você automatize o cálculo do salário de seus funcionários.
Para isso, você deverá fazer um programa que calcule o salário líquido de um
funcionário. O responsável pelo pagamento deverá fornecer ao programa a
quantidade de horas trabalhadas pelo funcionário durante o mês, o valor de sua hora
de trabalho, e a porcentagem de impostos cobrados sobre o salário. Ao final, o
programa deverá exibir o salário bruto do funcionário, o valor dos impostos cobrados
e o salário líquido.'''

salario_b = float(input("Digite a hora de trabalho do funcionario: "))
dia_trabalhado = salario_b * 8
dias_t = int(input("Digite quantos dias esse funcionario trabalhou no mês: "))
desconto = float(input("Qual a porcetagem de desconto esse funcionario terá: "))
salario_liquid = (dia_trabalhado * dias_t) * (desconto/100)
salario_total = (dia_trabalhado * dias_t) - salario_liquid

print(f"O funcionario recebe {dia_trabalhado} por dia, e recebe já com {desconto} de desconto do salario, o salario liquido desse funcionario é de {salario_total}")