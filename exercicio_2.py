print("2) Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo. Se não formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo algum, se a é o maior).")
print("")
print("Digite o primeiro valor: ")
print("")
valor_a = int(input())
print("")
print("Digite o segundo valor: ")
print("")
valor_b = int(input())
print("")
print("Digite o terceiro valor: ")
print("")
valor_c = int(input())


valida_negativo_1 = valor_b - valor_c
valida_negativo_2 = valor_a - valor_c
valida_negativo_3 = valor_a - valor_b
 
if valida_negativo_1  < 0:
    valida_negativo_1 = valida_negativo_1 * -1

if valida_negativo_2  < 0:
    valida_negativo_2 = valida_negativo_2 * -1
 
if valida_negativo_3  < 0:
    valida_negativo_3 = valida_negativo_3 * -1
          
if valida_negativo_1 < valor_a < valor_b + valor_c:
    if valida_negativo_2 < valor_b < valor_a + valor_c:
        if valida_negativo_3 < valor_c < valor_a + valor_b:

            #Fórmula de Heron: Cálculo da área de um triângulo qualquer
            p = (valor_a + valor_b + valor_c)/2                                           #Cálculo do Semi-perímetro
            area_triangulo = pow(p * (p - valor_a) * (p - valor_b) * (p - valor_c), 1/2)  #Cálculo da Área do triângulo

            print("É possível formar um triângulo, e sua área é: " + str(area_triangulo))

        else:
            print("Não é possível formar o triângulo com as valores informados( " + str(valor_a) + ", " + str(valor_b) + ", " + str(valor_c) + " ) " )
    else:
            print("Não é possível formar o triângulo com as valores informados( " + str(valor_a) + ", " + str(valor_b) + ", " + str(valor_c) + " ) " )
else:
            print("Não é possível formar o triângulo com as valores informados( " + str(valor_a) + ", " + str(valor_b) + ", " + str(valor_c) + " ) " )