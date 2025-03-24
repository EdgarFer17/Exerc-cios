numero = int(input("Digite um número menor que 1000: "))

if numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidade = numero % 10

    if centenas == 0:
        dezenas = (numero % 100) // 10
        if dezenas == 0:
            unidade = numero % 10
            if unidade == 0 or 1:
                print(f"{unidade} Unidade")
            else:
                print(f"{unidade} Unidades")
        elif dezenas == 1:
            unidade = numero % 10
            if unidade == 0:
                print(f"{dezenas} Dezena, {unidade} Unidades")
            else:
                print(f"{dezenas} Dezena, {unidade} Unidades")
        else:
            unidade = numero % 10
            if unidade == 0:
                print(f"{dezenas}: Dezenas, {unidade}: Unidades")

    if centenas == 1:
        dezenas = (numero % 100) // 10
        if dezenas != 0:
            unidade = numero % 10
            if unidade != 0:
                print(f"{centenas}: Centena, {dezenas}: Dezenas, {unidade}: Unidades")
    if centenas > 1:
        dezenas = (numero % 100) // 10
        if dezenas != 0:
            unidade = numero % 10
            if unidade != 0:
                print(f"{centenas} Centenas, {dezenas} Dezenas, {unidade} Unidades")


else:
    print("Insira um número menor que 1000! ")