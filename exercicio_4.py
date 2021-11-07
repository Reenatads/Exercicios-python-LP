###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo2 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

print("4) Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.")
print("")

var_entrada = int(input("Digite um número: "))                                  # Capturando valor de entrada
primos = []
 

for i in range(1, var_entrada + 1):                                             
    
    if var_entrada % i == 0 :
        primos.append(i) 
    else:
        pass   
        
        
            
if len(primos) == 2 :
                print("O número " + str(var_entrada) + " é primo.")
else:
                print("O número " + str(var_entrada) + " não é primo") 
    
         


        

            

    

