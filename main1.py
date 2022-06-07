from tkinter import *
from tkinter import filedialog
import re
from datetime import *
from tkinter import *
from tkinter.ttk import Notebook, Frame, Combobox, Radiobutton
import urllib.request
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates


def parsing(date):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        countries.append(childList[3].firstChild.nodeValue)
        valutues.append(float((childList[4].firstChild.nodeValue).replace(",", ".")) / float(childList[2].firstChild.nodeValue))
    return countries,valutues

def kurs(country,date):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if childList[3].firstChild.nodeValue == country:
                return float((childList[4].firstChild.nodeValue).replace(",", "."))
            # if child.nodeName == "Name":
            #     if child.childNodes[0].nodeValue == country:
            #         for childd in childList:
            #             if childd.nodeName == "Value":
            #                 value = childd.childNodes[0].nodeValue

def graf():
    periodd = ch_period.get()
    country = country_3.get()
    if per.get()==1:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master = grafic)
        raz = timedelta(days = 1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd=re.split(' - ',periodd)
        temp1 = datetime.strptime(periodd[1],"%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0],"%d/%m/%Y")
        while(temp1!=temp2+raz):
            k = kurs(country,temp1)
            k = float(k)
            x.append(datetime.strftime(temp1, "%d.%b"))
            y1 = round(k,2)
            y.append(y1)
            temp1+=raz
        fig.clear()
        matplotlib.pyplot.plot(x,y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row = 5,column = 5)
    if per.get() == 2:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=grafic)
        raz = timedelta(days=1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd = re.split(' - ', periodd)
        temp1 = datetime.strptime(periodd[1], "%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0], "%d/%m/%Y")
        while (temp1 != temp2):
            k = kurs(country, temp1)
            x1 = datetime.strftime(temp1, "%d")
            if x1 in x:
                x.append(datetime.strftime(temp1, "%d."))
            else:
                x.append(x1)
            y1 = round(k,2)
            y.append(y1)
            temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)
    if per.get() == 3:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=grafic)
        raz = timedelta(weeks = 1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd = re.split(' - ', periodd)
        temp1 = datetime.strptime(periodd[1], "%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0], "%d/%m/%Y")
        while (temp1 < temp2):
            k = kurs(country, temp1)
            if k!=None:
                k = float(k)
                x.append(datetime.strftime(temp1, "%d.%m"))
                y1 = round(k,2)
                y.append(y1)
                temp1 += raz
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)
    if per.get() == 4:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=grafic)
        raz = timedelta(weeks=4.4)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        periodd = re.split(' - ', periodd)
        temp1 = datetime.strptime(periodd[1], "%d/%m/%Y")
        temp2 = datetime.strptime(periodd[0], "%d/%m/%Y")
        while (temp1 < temp2 + raz):
            k = kurs(country, temp1)
            k = float(k)
            x.append(datetime.strftime(temp1, "%b.%y"))
            y1 = round(k,2)
            y.append(y1)
            temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y,'--')
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)



def period():
    if per.get()==1:
        periodscheck=[]
        now = date.today()
        temp = now
        delta = timedelta(weeks = 1)
        for i in range(4):
            string = ''
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string+=datetime.strftime(temp,"%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck
    if per.get()==2:
        periodscheck = []
        now = date.today()
        temp = now
        delta = timedelta(weeks = 4.4)
        for i in range(4):
            string = ''
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck
    if per.get()==3:
        periodscheck = []
        now = date.today()
        temp = now
        for i in range(4):
            ost = int(datetime.strftime(temp, "%m")) % 3
            delta = timedelta(weeks=ost * 4.4)
            string = ''
            temp = temp - delta
            string = temp.strftime("%d/%m/%Y") + ' - '
            delta = timedelta(weeks=13.2)
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck
    if per.get()==4:
        periodscheck = []
        now = date.today()
        temp = now
        delta = timedelta(weeks = 52)
        for i in range(4):
            string = ''
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        ch_period['values'] = periodscheck








def convert():
    x = country_1.get()
    y = country_2.get()
    z = money.get()
    z = float(z)
    y_index = countries.index(y)
    y1 = valutues[y_index]
    x_index = countries.index(x)
    x1 = valutues[x_index]
    if x == "Рубль":
        y_index = countries.index(y)
        y1 = valutues[y_index]
        res = round(z/y1, 3)
        result.configure(text=res)

    elif y == "Рубль":
        x_index = countries.index(x)
        x1 = valutues[x_index]
        res = round(z*x1, 3)
        result.configure(text = res)
    else:
        x = float(x1)
        y = float(y1)
        res = str(float((x * z) / y))
        result.configure(text=res)





window = Tk()
window.title("Конвертер валют")
window.minsize(width=500, height=200)
window.maxsize(width=1600, height=1000)
tab_control = Notebook(window)
calc = Frame(tab_control)
tab_control.add(calc, text="Калькулятор валют")

countries = []
valutues = []
countries = parsing(datetime.today())[0]
valutues = parsing(datetime.today())[1]
valutues.append(1.0)
countries.append('Рубль')
country_1 = Combobox(calc)
country_1.grid(row=0, column=0, padx=10, pady=10, ipadx=25)
country_1['values'] = countries
country_2 = Combobox(calc)
country_2.grid(row=1, column=0, padx=10, pady=10, ipadx=25)
country_2['values'] = countries
money = Entry(calc)
money.grid(row=0, column=1, pady=10, padx=10)
result = Label(calc, text="")
result.grid(row=1, column=1, pady=10, padx=10)
converter = Button(calc, text = "Конвертировать",command = convert)
converter.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 15)

grafic = Frame(tab_control)
tab_control.add(grafic, text = "Динамика курса")
set1 = Label(grafic, text = "Валюта")
set1.grid(row = 0, column = 0, ipadx = 25)
set2 = Label(grafic, text = "Период")
set2.grid(row = 0, column = 1, ipadx = 25)
set3 = Label(grafic, text = "Выбор периода")
set3.grid(row = 0, column = 2, ipadx = 25)
country_3 = Combobox(grafic)
country_3.grid(row=1, column=0, padx=10, pady=10, ipadx=25)
countries.remove('Рубль')
country_3['values'] = countries
per = IntVar()
periodscheck=[]
period1 = Radiobutton(grafic, text = 'Неделя', value = 1,variable= per,command=period)
period1.grid(row = 1, column = 1)
period2 = Radiobutton(grafic, text = 'Месяц', value = 2,variable= per, command=period)
period2.grid(row = 2, column = 1)
period3 = Radiobutton(grafic, text = 'Квартал', value = 3,variable= per,command=period)
period3.grid(row = 3, column = 1, pady = 10)
period4 = Radiobutton(grafic, text = 'Год', value = 4,variable= per, command=period)
period4.grid(row = 4, column = 1)
ch_period = Combobox(grafic)
ch_period.grid(row=1, column=2, padx=10, pady=10, ipadx=25,)
draw = Button(grafic, text = "Нарисовать график!",command = graf)
draw.grid(row = 4, column = 0, padx = 10, pady = 10, ipadx = 15)

print(countries)
print(valutues)



tab_control.pack(expand=True, fill=BOTH, side="top")
window.mainloop()