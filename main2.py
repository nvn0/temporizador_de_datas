# Version without classes

import numpy as np
import matplotlib.pyplot as plt
import os
import datetime




eventos_dic = {}
eventos_array = []

tday = datetime.date.today()
td = tday.strftime('%d/%m/%Y')
tdd = int(tday.strftime('%d'))
tdm = int(tday.strftime('%m'))
tdn = int(tday.strftime('%Y'))
print(tday.strftime('%d/%m/%Y'))



ficheiro = "lista de datas.txt"

if os.path.isfile(ficheiro):

    f = open(ficheiro, "r")
    linha = f.readline().strip()

    while linha != "":
        aux = linha.split("-")
        eventos_dic.update({aux[0]: [aux[1]]})
        linha = f.readline().strip()
    f.close()



def o1(): # Adicionar evento


    nome = input("Insira o nome do evento:")
    dta = input("Insira a data do evento(ex:20/08/2022):")

    eventos_dic.update({nome: [dta]})
    print(eventos_dic)




def o2():  # Visualizar datas
    print(eventos_dic)
    print(eventos_array)

    evento_mais_proximo = ""

    for x in eventos_dic.values():
        #print(x)
        if td - date(x):
            




opc = ""
while opc != "exit":

    print("\n==============================================================")
    print("                      MENU PRINCIPAL")
    print("==============================================================")
    print("[1] - Adicionar data")
    print("[2] - Visualizar datas")
    print("[exit] - Sair")
    print("==============================================================")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        o1()
    elif opc == "2":
        o2()
    elif opc == "exit":
        print("\nA sair...")

        f = open(ficheiro, "w")
        for p in eventos_dic:
            #print(p)
            f.write(p + " - " + str(eventos_dic[p][0]) + "\n")

        f.close()
    else:
        print("\nOpção inválida")










