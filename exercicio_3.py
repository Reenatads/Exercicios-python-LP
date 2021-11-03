###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo2 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

print("3) Faça um programa que leia 3 números inteiros e mostre o menor deles.")
print("")
print("Digite o primeiro número: ")
print("")
valor_um = int(input())
print("Digite o segundo número: ")
print("")
valor_dois = int(input())
print("")
print("Digite o terceiro número: ")
print("")
valor_tres = int(input())
print("")

if valor_um <= valor_dois and valor_um <= valor_tres:     #Validando se o menor valor foi o primeiro a ser digitado.
    menor_numero = valor_um    
if valor_dois <= valor_um and valor_dois <= valor_tres:   #Validando se o menor valor foi o segundo a ser digitado.
    menor_numero = valor_dois
if valor_tres <= valor_um and valor_tres <= valor_dois:   #Validando se o menor valor foi o terceiro a ser digitado.
    menor_numero = valor_tres

print("O menor valor é: " + str(menor_numero))