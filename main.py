# Version with dataclasses

from dataclasses import dataclass

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
        aux = linha.split("/")
        eventos_dic.update({aux[0]: [aux[1]]})
        linha = f.readline().strip()
    f.close()






# V1:
@dataclass
class evento:
    nome: str
    dia: int
    mes: int
    ano: int

# V2:

# class Evento:
#     def __init__(self, nome, dia, mes, ano):
#         self.nome = nome
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano
#
#     def GetInfo(self):
#         print(self.nome, " - ", self.dia, "/", self.mes, "/", self.ano)
#
#     def GetNome(self):
#         return self.nome
#
#
#     def GetDia(self):
#         return self.dia
#
#     def GetMes(self):
#         return self.mes
#
#
#     def GetAno(self):
#         return self.ano








def o1(): # Adicionar evento

    # V1:
    # nome = input("Insira o nome do evento:")
    # dta = input("Insira a data do evento(ex:20/08/2022):")
    #
    # eventos.update({nome: [dta]})
    # print(eventos)

    # V2:
    nome = input("Insira o nome do evento:")
    d = int(input("Insira o dia do evento:"))
    m = int(input("Insira o mes do evento:"))
    a = int(input("Insira o ano do evento:"))

    x = evento(nome, d, m, a)
    eventos_array.append(x)
    print("Evento adicionado!")



def o2(): # Visualizar datas
    print(eventos_dic)
    print(eventos_array)


    evento_mais_proximo = ""

    min_ano = min(evento.ano for evento in eventos_array)
    print(min_ano)


    for evento in eventos_array:
        if tdn > evento.ano:
            evento_mais_proximo = evento.nome
            break
        elif tdn == evento.ano:
            if tdm > evento.mes:
                evento_mais_proximo = evento.nome
                break
            elif tdm == evento.mes:
                if tdd > evento.dia:
                    evento_mais_proximo = evento.nome
                    break
            elif tdm < evento.mes:

    print(evento_mais_proximo)




    # fig, axs = plt.subplots(2,2)
    # axs[0, 0].bar()
    # axs[0, 0].set_title("Tempo restante")
    #
    # fig.tight_layout()
    # plt.show()

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













