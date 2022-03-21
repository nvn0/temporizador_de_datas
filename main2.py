# Version without classes


from datetime import date
import datetime
import pickle
import os
import datetime
import platform
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

clear_command = "cls" if platform.system() == "Windows" else "clear"

eventos_dic = {}



# try:
#     with open('lista de eventos2.pkl', 'rb') as load_file:
#         eventos_dic = pickle.load(load_file)
#         #print(eventos_dic)
# except:
#     pass





tday = datetime.date.today()
td = tday.strftime('%d/%m/%Y')
tdd = int(tday.strftime('%d'))
tdm = int(tday.strftime('%m'))
tdn = int(tday.strftime('%Y'))
#print(tday.strftime('%d/%m/%Y'))



ficheiro = "lista de datas.txt"

if os.path.isfile(ficheiro):

    f = open(ficheiro, "r")
    linha = f.readline().strip()

    while linha != "":
        aux = linha.split("/")
        eventos_dic.update({aux[0]: [int(aux[1]), int(aux[2]), int(aux[3])]})
        linha = f.readline().strip()
    f.close()



def o1(): # Adicionar evento


    nome = input("Insira o nome do evento:")
    d = int(input("Insira o dia do evento:"))
    m = int(input("Insira o mes do evento:"))
    a = int(input("Insira o ano do evento:"))

    eventos_dic.update({nome: [d, m, a]})
    print(eventos_dic)




def o2():  # Visualizar datas
    next_eventos = []
    #print(eventos_dic)

    # for i in eventos_dic:
    #     print(len(eventos_dic[i]))


    # adicionar tempo as datas
    for i in eventos_dic:
        if (len(eventos_dic[i])) < 4:
            x = date(eventos_dic[i][2], eventos_dic[i][1], eventos_dic[i][0])
            x2 = date(tdn, tdm, tdd)
            dif = x - x2
            eventos_dic[i].append(dif)
            next_eventos.append(dif)
            #print(dif)
        else:
            continue

    #print(eventos_dic)



    # Remover Eventos passados
    for i in eventos_dic.keys():
        if eventos_dic[i][2] < tdn:
            eventos_dic.pop(i)
            break
        elif eventos_dic[i][2] == tdn:
            if eventos_dic[i][1] < tdm:
                eventos_dic.pop(i)
                break
            elif eventos_dic[i][1] == tdm:
                if eventos_dic[i][0] < tdd:
                    eventos_dic.pop(i)
                    break



    #print(eventos_dic)



    # Calcular evento mais proximo
    evento_mais_proximo = list(eventos_dic.keys())[0]
    for i in eventos_dic:
        if eventos_dic[i][3] < eventos_dic[evento_mais_proximo][3]:
            evento_mais_proximo = i
    print("\nO evento mais próximo é o", Fore.RED + evento_mais_proximo, "dentro de", Fore.RED + str(eventos_dic[evento_mais_proximo][3]), "dia:", eventos_dic[evento_mais_proximo][0], "/", eventos_dic[evento_mais_proximo][1], "/", eventos_dic[evento_mais_proximo][2])


    next_eventos.sort()

    nxev =[]
    for x in next_eventos:
        for m, i in eventos_dic.items():
            if x in i:
                nxev.append(m)

    # print(nxev)
    # print('\n'.join(map(str, nxev)))

    print("\n")

    count = 1
    for e in nxev:
        dias = eventos_dic[e][3]
        print(count, Fore.YELLOW + e, "dentro de", Fore.YELLOW + str(dias), "(dia:",eventos_dic[e][0], "/",eventos_dic[e][1], "/",eventos_dic[e][2], ")")
        count += 1
        #print(e, "dentro de", eventos_dic[e][3])





opc = ""
while opc != "exit":

    print("\n==============================================================")
    print("                      MENU PRINCIPAL")
    print("==============================================================")
    print("[1] - Adicionar Evento")
    print("[2] - Visualizar Eventos")
    print("[exit] - Sair")
    print("==============================================================")

    opc = input("\nEscolha uma opção: ")

    if opc == "1":
        os.system(clear_command)
        print("Adicionar Evento")
        o1()
    elif opc == "000":
        exit()
    elif opc == "2":
        os.system(clear_command)
        print("Visualizar Eventos")
        o2()
    elif opc == "exit":
        print("\nA sair...")

        # with open('lista de eventos2.pkl', 'wb') as file:
        #     pickle.dump(eventos_dic, file)

        f = open(ficheiro, "w")

        for p in eventos_dic:
            f.write(p + "/" + str(eventos_dic[p][0]) + "/" + str(eventos_dic[p][1]) + "/" + str(eventos_dic[p][2]) + "\n")

        f.close()

    else:
        print(Fore.RED + "\nERRO! - Opção inválida")


