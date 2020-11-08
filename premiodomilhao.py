num_dias = int(input("Informe o número de dias: "))

cont_dias = 1
cont_valor = 0
aux = 1

for x in range(num_dias):
    valor_dia = int(input("Qual o valor do {}º Dia: ".format(aux)))
    cont_valor += valor_dia 

    if cont_valor < 1000000:
        cont_dias += 1

    aux += 1

print(cont_dias)

