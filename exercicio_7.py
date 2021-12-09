###################################################
### Aluna: Renata dos Santos. Atividade: Ciclo5 ###
### Universidade: UNIS - MG                     ###
### Disciplina: Linguagens de programação       ###
### Ano: 2021                                   ###
###################################################

                                            
import sqlite3                                  #Importando biblioteca para conexão com BD
from sqlite3 import Error

connection = sqlite3.connect('imc.db')          #Criando conexão
c = connection.cursor()
# Criando conexão
def ConexaoBanco():
    caminho = "C:\\Users\\reds\\Downloads\\SQLiteStudio\\imc_db.db" #Caminho onde salvo o BD criado no SQLITE na minha máquina
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()
                                                                   #Criando tabela
vsql="""  CREATE TABLE IF NOT EXISTS tb_imc(
                ID_PACIENTE INTEGER PRIMARY KEY AUTOINCREMENT, 
                NOME_PACIENTE  VARCHAR(30),
                ENDERECO_PACIENTE VARCHAR(30),
                ALTURA_PACIENTE FLOAT,
                PESO_PACIENTE FLOAT,
                IMC_PACIENTE FLOAT
);"""   

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)
                                                                    #Inserindo dados na tabela
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

                                                                    #Definindo dados de entrada
name = str(input('Qual o nome completo do paciente? : '))
adress = str(input('Qual o endereco do paciente? : '))
wheight = float(input('Qual é o peso do paciente? (KG) : '))
hight = float(input('Qual é a altura paciente? (m) : '))
imc = wheight/ (hight ** 2)
print(('O IMC é : {:.1f}'.format(imc)))

wheight = str(wheight)
hight = str(hight)
imc = str("{:.1f}".format(imc))
                                                                 #Inserindo dados na tabela
vsql="INSERT INTO tb_imc ( NOME_PACIENTE,        ENDERECO_PACIENTE, ALTURA_PACIENTE, PESO_PACIENTE, IMC_PACIENTE) VALUES ('"+name+"', '"+adress+"', "+wheight+", '"+hight+"', "+imc+")"
inserir(vcon, vsql)

criarTabela(vcon,vsql)
vcon.close()