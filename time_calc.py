from datetime import date
import datetime


tday = datetime.date.today()
td = tday.strftime('%d/%m/%Y')
td2 = tday.strftime('%Y,%m,%d')
tdd = int(tday.strftime('%d'))
tdm = int(tday.strftime('%m'))
tdn = int(tday.strftime('%Y'))
print(tday.strftime('%d/%m/%Y'))



d = int(input("Insira o dia do evento:"))
m = int(input("Insira o mes do evento:"))
a = int(input("Insira o ano do evento:"))


x = date(a, m, d)
x2 = date(tdn, tdm, tdd)

dif = x - x2

print(dif)



