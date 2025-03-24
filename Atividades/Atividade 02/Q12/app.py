''' Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''

valor_hora = float(input("Digite o valor da sua hora: "))
qnt_horas = int(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = int(qnt_horas) * (valor_hora)
desconto_sindicato = 0.03

if salario_bruto <= 900 :
    desconto = 0
    salario_liquido = salario_bruto - desconto
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto = salario_bruto + 0.5
    salario_liquido =  salario_bruto -  desconto
elif salario_bruto >1500 and salario_bruto <=2500:
    desconto = salario_bruto * 0.10
else:
    desconto = salario_bruto *0.20
    salario_liquido = salario_bruto - desconto

print   (salario_liquido)