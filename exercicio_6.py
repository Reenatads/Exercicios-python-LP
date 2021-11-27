###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo3 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

                                                                  
from tkinter import *  # Importando o pacote tkinter para criação da inteface gráfica          

root = Tk()                                              
root.geometry("600x240+0+0") #Define o tamanho da janela
root.resizable(0,0)
root.title("Cálculo IMC - indice de Massa Corporal")  #Define o nome da janela
 
var1 = StringVar()  #Variável para armazenar o nome do paciente                                  
var2 = StringVar()  #Variável para armazenar o endereço do paciente
var3 = DoubleVar()  #Variável para armazenar a altura do paciente
var4 = DoubleVar()  #Variável para armazenar o peso do paciente

def calculator():   #Função que realiza o cálculo do IMC
    imc_weight = float(var4.get())
    imc_height = float(var3.get())
    IMC = str('%2.f' % (imc_weight/(imc_height * imc_height))) 
    lblresult.config(text=IMC) #Atribuindo o valor do IMC na label de resultado

def reset():        #Função que limpa toso os campos preenchidos na janela
    txtname.delete  (0,"end")
    txtadress.delete(0,"end")
    txtheight.delete(0,"end")
    txtweight.delete(0,"end")

Tops = Frame (root, width = 600, height = 50, bd = 2, relief ="groove")  #Define o frame da parte superior da janela
Tops.pack(side=TOP)

f1 = Frame(root, width = 600, height = 600, bd = 2 , relief = "groove" ) #Define o frame que armazena os campos de nome e endereço
f1.pack(fill=BOTH)

f2 = Frame(root, width = 300, height = 150, bd = 2 , relief = "groove" ) #Define o frame que armazena os campos de peso, altura e os botões de ação.
f2.pack(side=LEFT)

f3 = Frame(root, width = 300, height = 150, bd = 2 , relief = "groove" ) #Define o frame de arzena o resultado do IMC
f3.pack(side=RIGHT)


lblTitle = Label(Tops, text = "Índice de Massa Corporal", padx=600, pady=4, bd=6, fg="gray21", font=("Arial", 16, 'bold'), bg = "thistle3", relief="groove",width = 32, height = 1)                                                                                             
lblTitle.pack() 

lblname   = Label( f1, text = "Nome do paciente:", bd = 4, font=("arial",12)).grid(sticky = "w",row=0, column=0)

lbladress = Label( f1, text = "Endereço Completo:", bd = 4, font=("arial",12)).grid(sticky = "w",row=1, column=0)

lblheight = Label( f2, text = "Altura (m):", bd = 4,font = ("arial",12),pady=6).grid(sticky = "w",row=2, column=0)

lblweight = Label( f2, text = "Peso (Kg):", bd = 4,font = ("arial",12),pady=6).grid(sticky = "w",row=3, column=0)

lblresult = Label(f3, padx=103, pady=50,bd=4, font=("arial",12, "bold"), bg="thistle3", relief = "sunk", width = 10, height = 1)
lblresult.grid(sticky = "w",row = 0, column=3)


txtname =   Entry(f1, textvariable=var1, font=("arial",12), bd=4, width=48, justify="left")
txtname.grid(row = 0, column=2)

txtadress = Entry(f1, textvariable=var2, font=("arial",12), bd=4, width=48, justify="left")
txtadress.grid(row = 1, column=2)

txtheight = Entry(f2, textvariable=var3, font=("arial",12), bd=4, width=20, justify="left")
txtheight.grid(row = 2, column=2,sticky = "w")

txtweight = Entry(f2, textvariable=var4, font=("arial",12), bd=4, width=20, justify="left")
txtweight.grid(row = 3, column=2,sticky = "w")


f4 = Frame(f2)
f4.grid(row=4, column=0, pady = 10, sticky = "w")                       #Frame para os botões de ação

cal_btn = Button(f4,   text = 'Calcular', command = calculator)         #Definindo botão para efetuar o cálculo do IMC              
cal_btn.pack(side=LEFT)

reset_btn = Button(f4, text = 'Reset', command = reset)                 #Definindo botão de reset
reset_btn.pack(side=LEFT)

exit_btn = Button(f4,  text = 'Sair', command = lambda:root.destroy())  #Define botão de saída
exit_btn.pack(side=RIGHT)

root.mainloop()                                                         #Loop da janela