'''Construa um algoritmo que mostre a velocidade média de um carro após ele ter
percorrido uma distância d em um intervalo de tempo t fornecidos pelo usuário.'''

dist = int(input("Digite a distancia em mestros que o carro percorreu: "))
temp = float(input("Digite o tempo que você levou para chegar ao destino: "))

v = dist/temp

print(f"Sua velocidade media foi {v}m/s ")