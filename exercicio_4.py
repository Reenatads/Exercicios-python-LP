###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo2 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

print("4) Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.")
print("")

var_final = 100
num_divisoes = 0

for i in range(var_inicio, var_final + 1):
    if var_inicio % i == 0 :
        print("O número " + str(var_inicio) + " é primo.")
    else:   
        if var_inicio % 2 != 0:
            print("O número " + str(var_inicio) + " é primo.")

    

