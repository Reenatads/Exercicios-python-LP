###################################################
### ALUNA: Renata dos Santos. Atividade: Ciclo2 ###
###################################################

#1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

print("Bem-Vindo a atividade do ciclo 2!")
print("")
print("1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.")
print("")
print("Digite uma idade em dias: ")
print("")
idade_dias  = int(input())                #Idade em Dias
idade_anos  = int(idade_dias / 365)       #Idade em Anos
idade_meses = int(idade_dias / 30)        #Idade em Meses
print("A idade " + str(idade_dias) +" em Anos é: " + str(idade_anos))
print("")   
print("A idade " + str(idade_dias) +" em Meses é: " + str(idade_meses))


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
            print("É possível formar um triângulo, e sua área é: " + valor_a)

        

