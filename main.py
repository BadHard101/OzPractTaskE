import re
from datetime import *
from tkinter import *
from tkinter.ttk import Notebook, Frame, Combobox, Radiobutton
import urllib.request
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates


def parsing_countries(date):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if child.nodeName == "Name":
                Countries.append(child.childNodes[0].nodeValue)
            if child.nodeName == "Value":
                Valutues.append(child.childNodes[0].nodeValue)
    return Countries, Valutues

def parsing_value(country, date):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + datetime.strftime(date, "%d/%m/%Y"))
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")
    for node in nodeArray:
        childList = node.childNodes
        for child in childList:
            if child.nodeName == "Name":
                if child.childNodes[0].nodeValue == country:
                    for childd in childList:
                        if childd.nodeName == "Value":
                            value = childd.childNodes[0].nodeValue
    return value

def print_graf():
    period = CB_Periods.get()
    country = CB_Country3.get()
    if RadioB_Sellector.get()==1:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = Grafic)
        raz = timedelta(days = 1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        period=re.split(' - ',period)
        temp1 = datetime.strptime(period[1],"%d/%m/%Y")
        temp2 = datetime.strptime(period[0],"%d/%m/%Y")
        while(temp1!=temp2+raz):
            k = parsing_value(country, temp1)
            k = k.replace(',','.')
            k = float(k)
            print(k)
            x.append(datetime.strftime(temp1, "%d.%b"))
            y1 = round(k,2)
            y.append(y1)
            temp1+=raz
        fig.clear()
        matplotlib.pyplot.plot(x,y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row = 5,column = 5)
    if RadioB_Sellector.get() == 2:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=Grafic)
        raz = timedelta(days=1)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        period = re.split(' - ', period)
        temp1 = datetime.strptime(period[1], "%d/%m/%Y")
        temp2 = datetime.strptime(period[0], "%d/%m/%Y")
        while (temp1 != temp2 + raz):
            k = parsing_value(country, temp1)
            k = k.replace(',', '.')
            k = float(k)
            if (datetime.strftime(temp1, "%d")) in x:
                x.append(datetime.strftime(temp1, "%d."))
            else:
                x.append(datetime.strftime(temp1, "%d"))
            y1 = round(k,2)
            y.append(y1)
            temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)
    if RadioB_Sellector.get() == 3:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=Grafic)
        raz = timedelta(weeks = 2)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        period = re.split(' - ', period)
        temp1 = datetime.strptime(period[1], "%d/%m/%Y")
        temp2 = datetime.strptime(period[0], "%d/%m/%Y")
        while (temp1 < temp2):
            k = parsing_value(country, temp1)
            if k!=None:
                k = k.replace(',', '.')
                k = float(k)
                x.append(datetime.strftime(temp1, "%d.%m.%y"))
                y1 = round(k,2)
                y.append(y1)
                temp1 += raz
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)
    if RadioB_Sellector.get() == 4:
        matplotlib.use('TkAgg')
        fig = matplotlib.pyplot.figure(figsize=(10, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=Grafic)
        raz = timedelta(weeks=4.4)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        x = []
        y = []
        period = re.split(' - ', period)
        temp1 = datetime.strptime(period[1], "%d/%m/%Y")
        temp2 = datetime.strptime(period[0], "%d/%m/%Y")
        while (temp1 < temp2 + raz):
            k = parsing_value(country, temp1)
            k = k.replace(',', '.')
            k = float(k)
            x.append(datetime.strftime(temp1, "%b.%y"))
            y1 = round(k,2)
            y.append(y1)
            temp1 += raz
        fig.clear()
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.grid()
        plot_widget.grid(row=5, column=5)



def sellect_period():
    periodscheck = []
    now = date.today()
    temp = now
    flag = True

    if RadioB_Sellector.get()==1:
        delta = timedelta(weeks = 1)
    elif RadioB_Sellector.get()==2:
        delta = timedelta(weeks = 4.4)
    elif RadioB_Sellector.get() == 3:
        for i in range(4):
            ost = int(datetime.strftime(temp, "%m")) % 3
            delta = timedelta(weeks=ost * 4.4)
            temp = temp - delta
            string = temp.strftime("%d/%m/%Y") + ' - '
            delta = timedelta(weeks=13.2)
            temp = temp - delta
            string += datetime.strftime(temp, "%d/%m/%Y")
            periodscheck.append(string)
        CB_Periods['values'] = periodscheck
        flag = False
    elif RadioB_Sellector.get()==4:
        delta = timedelta(weeks = 52)

    if flag:
        for i in range(4):
            string = temp.strftime("%d/%m/%Y") + ' - '
            temp = temp - delta
            string+=datetime.strftime(temp,"%d/%m/%Y")
            periodscheck.append(string)
        CB_Periods['values'] = periodscheck

def convert_value():
    x = CB_Country1.get()
    y = CB_Country2.get()
    z = ToConvertField_Entry.get()

    x = Valutues[Countries.index(x)]
    y = Valutues[Countries.index(y)]

    x = float(x.replace(',','.'))
    y = float(y.replace(',', '.'))
    z = float(z)

    res = "Converted: " + str(round(float((x*z)/y),2))
    ConvertedField_Label.configure(text = res)


"""
Описываем весь Layout
"""
Countries = []
Valutues = []

App = Tk()
Controller = Notebook(App)
Calculator = Frame(Controller)
CB_Country1 = Combobox(Calculator)
CB_Country2 = Combobox(Calculator)
Grafic = Frame(Controller)
CB_Country3 = Combobox(Grafic)

ToConvertField_Entry = Entry(Calculator)
ConvertedField_Label = Label(Calculator, text="")
RadioB_Sellector = IntVar()

CB_Periods = Combobox(Grafic)
Button_Draw = Button(Grafic, text="Нарисовать график!", command=print_graf)
Button_Convert = Button(Calculator, text="Конвертировать", command=convert_value)


def main():

    App.title("Конвертер валют")
    App.minsize(width=500, height=200)
    App.maxsize(width=1600, height=1000)


    Controller.add(Calculator, text="Калькулятор валют")

    Countries = parsing_countries(datetime.today())[0]

    CB_Country1.grid(row=0, column=0, padx=10, pady=10, ipadx=25)
    CB_Country1['values'] = Countries

    CB_Country2.grid(row=1, column=0, padx=10, pady=10, ipadx=25)
    CB_Country2['values'] = Countries

    ToConvertField_Entry.grid(row=0, column=1, pady=10, padx=10)
    ConvertedField_Label.grid(row=1, column=1, pady=10, padx=10)
    Button_Convert.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 15)

    Controller.add(Grafic, text ="Динамика курса")
    Value_Label = Label(Grafic, text ="Валюта")
    Value_Label.grid(row = 0, column = 0, ipadx = 25)
    RBPeriod_Label = Label(Grafic, text ="Период")
    RBPeriod_Label.grid(row = 0, column = 1, ipadx = 25)
    CBPeriod_Label = Label(Grafic, text ="Выбор периода")
    CBPeriod_Label.grid(row = 0, column = 2, ipadx = 25)

    CB_Country3.grid(row=1, column=0, padx=10, pady=10, ipadx=25)
    CB_Country3['values'] = Countries

    RB_WeekPeriod = Radiobutton(Grafic, text='Неделя', value=1, variable=RadioB_Sellector, command=sellect_period)
    RB_WeekPeriod.grid(row = 1, column = 1)
    RB_MonthPeriod = Radiobutton(Grafic, text ='Месяц', value = 2, variable= RadioB_Sellector, command=sellect_period)
    RB_MonthPeriod.grid(row = 2, column = 1)
    RB_QuoterPeriod = Radiobutton(Grafic, text ='Квартал', value = 3, variable= RadioB_Sellector, command=sellect_period)
    RB_QuoterPeriod.grid(row = 3, column = 1, pady = 10)
    RB_YearPeriod = Radiobutton(Grafic, text ='Год', value = 4, variable= RadioB_Sellector, command=sellect_period)
    RB_YearPeriod.grid(row = 4, column = 1)

    CB_Periods.grid(row=1, column=2, padx=10, pady=10, ipadx=25, )
    Button_Draw.grid(row = 3, column = 2, padx = 10, pady = 10, ipadx = 15)

    Controller.pack(expand=True, fill=BOTH, side="top")
    App.mainloop()

if __name__=='__main__':
    main()