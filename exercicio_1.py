###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo2 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

#1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

print("Bem-Vindo a atividade do ciclo 2!")
print("")
print("1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.")
print("")
print("Digite uma idade em dias: ")
print("")
idade_dias  = int(input())                #Idade em Dias.
idade_anos  = int(idade_dias / 365)       #Idade em Anos.
idade_meses = int(idade_dias / 30)        #Idade em Meses.
print("A idade " + str(idade_dias) +" em Anos é: " + str(idade_anos))
print("")   
print("A idade " + str(idade_dias) +" em Meses é: " + str(idade_meses))


