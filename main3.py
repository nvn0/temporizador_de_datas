# Version with normal clases

import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime



eventos_dic = {}
eventos_array = []


try:
    with open('lista de eventos3.pkl', 'rb') as load_file:
        eventos_dic = pickle.load(load_file)
        #print(eventos_dic)
except:
    pass



try:
    with open('lista de eventos33.pkl', 'rb') as inp:
        eventos_array = pickle.load(inp)
        #print(eventos_array)
except:
    pass




tday = datetime.date.today()
td = tday.strftime('%d/%m/%Y')
tdd = int(tday.strftime('%d'))
tdm = int(tday.strftime('%m'))
tdn = int(tday.strftime('%Y'))
print(tday.strftime('%d/%m/%Y'))





class Evento:
    def __init__(self, nome, dia, mes, ano):
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def GetInfo(self):
        print(self.nome, "-", self.dia, "/", self.mes, "/", self.ano)

    def GetNome(self):
        return self.nome


    def GetDia(self):
        return self.dia

    def GetMes(self):
        return self.mes


    def GetAno(self):
        return self.ano



def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def load_object(obj, filename):
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    print(obj.GetInfo())


def o1(): # Adicionar evento


    nome = input("Insira o nome do evento:")
    d = int(input("Insira o dia do evento:"))
    m = int(input("Insira o mes do evento:"))
    a = int(input("Insira o ano do evento:"))

    obj = Evento(nome, d, m, a)
    eventos_array.append(obj)
    eventos_dic.update({nome:[d, m, a]})

    file_name = input("Introduza o nome do ficheiro para este objeto:")

    save_object(obj, f"{file_name}")


    print("Evento adicionado!")



def o2(): # Visualizar datas
    print(eventos_dic)
    print(eventos_array)

    #print(eventos_array)
    evento_mais_proximo = ""



    # for evento in eventos_array:
    #     if tdn > Evento.GetAno():
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
    #
    # print(evento_mais_proximo)




    # fig, axs = plt.subplots(2,2)
    # axs[0, 0].bar()
    # axs[0, 0].set_title("Tempo restante")
    #
    # fig.tight_layout()
    # plt.show()




def o3():

    o = input("insira o nome do objeto:")
    fn = input("Insira o nome do ficheiro do objeto:")

    load_object(o, fn)





opc = ""
while opc != "exit":

    print("\n==============================================================")
    print("                      MENU PRINCIPAL")
    print("==============================================================")
    print("[1] - Adicionar evento")
    print("[2] - Visualizar eventos")
    print("[3] - Load objeto(evento)")
    print("[exit] - Sair")
    print("==============================================================")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        o1()
    elif opc == "2":
        o2()
    elif opc == "3":
        o3()
    elif opc == "exit":
        print("\nA sair...")

        with open('lista de eventos3.pkl', 'wb') as file:
            pickle.dump(eventos_dic, file)

        #save_object(eventos_array, 'lista de eventos33.pkl')

    else:
        print("\nOpção inválida")







