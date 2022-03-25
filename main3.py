# Version with normal clases

import json
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime



eventos_dic = {}



try:
    with open('lista de eventos.json', 'r') as file:
        json_obj = json.loads(file.read())
        eventos_dic.update(json_obj)
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


    def add_to_dict(self):
        evento_obj = {'nome': self.nome, 'dia': self.dia, 'mes': self.mes, 'ano': self.ano}
        #eventos_dic.update(evento_obj)
        eventos_dic["Eventos"].append(evento_obj)





def o1(): # Adicionar evento


    nome = input("Insira o nome do evento:")
    d = int(input("Insira o dia do evento:"))
    m = int(input("Insira o mes do evento:"))
    a = int(input("Insira o ano do evento:"))

    obj = Evento(nome, d, m, a)
    obj.add_to_dict()



    print("Evento adicionado!")
    print(eventos_dic)
    print(eventos_dic['Eventos'][0]['nome'])

def o2(): # Visualizar datas
    print(eventos_dic)

    for i in eventos_dic['Eventos']:
        print(i)










opc = ""
while opc != "exit":

    print("\n==============================================================")
    print("                      MENU PRINCIPAL")
    print("==============================================================")
    print("[1] - Adicionar evento")
    print("[2] - Visualizar eventos")
    print("[exit] - Sair")
    print("==============================================================")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        o1()
    elif opc == "2":
        o2()
    elif opc == "exit":
        print("\nA sair...")

        json_string = json.dumps(eventos_dic, indent=2)
        with open('lista de eventos.json', 'w') as file:
            file.write(json_string)

    else:
        print("\nOpção inválida")







