###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo2 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

print("5) Escreva uma função que: a) Receba uma frase como parâmetro. b) Retorne uma nova frase com cada palavra com as letras invertidas.")
print("")

def inverte(frase):
    frase_invertida = ""
    for i in frase:
        frase_invertida = i + frase_invertida
    print("A frase com as letras invertidas é: ", frase_invertida)

frase = input("Escreva a frase: ")
print("")
print("Frase inserida: ", frase)
print("")
inverte(frase)