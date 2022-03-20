# Version with dataclasses

from dataclasses import dataclass
import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

eventos_dic = {}
eventos_array = []


try:

    with open('lista de eventos.txt', 'r') as load_file:
        #linec = load_file.readline().replace(""","")
        for line in load_file:
            eventos_array.append(line)
        #print(eventos_array)
except:
    pass

tday = datetime.date.today()
td = tday.strftime('%d/%m/%Y')
tdd = int(tday.strftime('%d'))
tdm = int(tday.strftime('%m'))
tdn = int(tday.strftime('%Y'))
print(tday.strftime('%d/%m/%Y'))










# V1:
@dataclass
class evento:
    nome: str
    dia: int
    mes: int
    ano: int






def o1(): # Adicionar evento


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


    # evento_mais_proximo = ""
    #
    # min_ano = min(evento.ano for evento in eventos_array)
    # print(min_ano)
    #
    #
    # for evento in eventos_array:
    #     if tdn > evento.ano:
    #         evento_mais_proximo = evento.nome
    #         break
    #     elif tdn == evento.ano:
    #         if tdm > evento.mes:
    #             evento_mais_proximo = evento.nome
    #             break
    #         elif tdm == evento.mes:
    #             if tdd > evento.dia:
    #                 evento_mais_proximo = evento.nome
    #                 break
    #         elif tdm < evento.mes:
    #             evento_mais_proximo = evento.nome
    #
    # print(evento_mais_proximo)




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

        with open('lista de eventos.txt', 'w') as file:
            for i in eventos_array:
                file.write(str(i))

    else:
        print("\nOpção inválida")













