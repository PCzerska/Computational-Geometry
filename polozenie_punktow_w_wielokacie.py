from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import colorchooser
import numpy as np
from numpy import rad2deg
from math import atan2, pi, degrees
minx=0
maxx=0
miny=0
maxy=0
pktx=[]
pkty=[]
iksy=[]
igreki=[]
angles=[]
window = Tk()
window.title("Paulina Czerska GI")
window.geometry('1350x900')
window.configure(background='pink')
punkciki=[]
do_rysunku=[]

Yk=[]
Xk=[]
xd=[]
yd=[]
dod_punkty=[]
x=[]
y=[]
spr=[]
SUMY=[]
wierzcholki=[]
color='pink'
colorpunktow='red'

def kolor_punktow():
    global colorpunktow
    x = colorchooser.askcolor()[1]
    colorpunktow = x
    wykres1(grubosc)
    return colorpunktow



def bbox():
    ixy = []
    iyy = []
    for i in punkciki:
        ixy.append(i[1])
        iyy.append(i[0])
    global minx,maxx,miny,maxy
    minx = min(ixy)
    maxx = max(ixy)
    miny = min(iyy)
    maxy = max(iyy)

    return minx, maxx, miny, maxy



def inbbox(punkt):

    if float(punkt[1]) < float(minx) or float(punkt[1]) > float(maxx) or float(punkt[0]) < float(miny) or float(
            punkt[0]) > float(maxy):
        return False
    else:
        return True

def wczytaj_dane():
    file = filedialog.askopenfilename()
    f = open(file, "r").read()
    lines = f.split('\n')
    global punkciki
    punkty= []
    for line in lines:
        if line != '':
            line=line.split('       ')
            punkty.append(line)
    punkciki=punkty
    return punkciki


def wczytaj_punkty():
    global iksy, igreki

    plik = filedialog.askopenfilename()
    p = open(plik, "r").read()
    lines = p.split('\n')
    bbox()

    global x, y
    for line in lines:
        if line != '':
            line = line.split(' ')
            punkt=[float(line[1]),float(line[0])]
            if inbbox(punkt)==True:
                y.append(float(line[0]))
                x.append(float(line[1]))

    iksy = x
    igreki = y

    return iksy, igreki, print('yep')



def sprawdzam(iksy, igreki):
    pkt = []
    global xd,yd
    xd=[]
    yd=[]
    global colorpunktow,colorpunktow1
    for r in range(len(iksy)):
        angle = []
        wektory = []

        for i in range(len(punkciki)):
            a1 = [float(punkciki[i][0]), float(punkciki[i][1])]
            w1 = [float(a1[0]) - float(iksy[r]), float(a1[1]) - float(igreki[r])]
            wektory.append(w1)

            if a1[0] == iksy[r] and a1[1]==igreki[r]:
                pkt.append([iksy[r], igreki[r]])
                break




        for t in range(len(wektory) - 1):
            angle.append(np.arctan2(wektory[t][0], wektory[t][1]) - np.arctan2(wektory[t + 1][0], wektory[t + 1][1]))

            if angle[t] < -np.pi:
                angle[t] += 2 * np.pi
            if angle[t] > np.pi:
                angle[t] -= 2 * np.pi

        angle = rad2deg(angle)

        s = sum(angle)

        if abs(s) >= 359.999 and abs(s) <= 360.001:
            s = 360

        if s == 360:

            pkt.append([iksy[r], igreki[r]])
            pktx.append(float(iksy[r]))
            pkty.append(float(igreki[r]))

    dlug="ilość punktów w wielokącie: " + str(len(pkt))
    txt6.insert(0,dlug)
    return pkt, print(pkt)


def podzial_punktow():
    wczytaj_dane()
    global Yk, Xk
    Y= []
    X= []
    for ev in punkciki:
        Y.append(float(ev[0]))
        X.append(float(ev[1]))
    Yk= Y
    Xk= X
    return Yk,Xk

fig=plt.figure(figsize=(8,7))
plt.title('Położenie wielokąta i punktów', font='Arial', fontsize='20')
plt.xticks(np.arange(0,100,10))
plt.yticks(np.arange(0,100,10))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=0, column=0,rowspan=5, padx=15, pady=15)
canvas.draw()

def wykres():
    fig = plt.figure(figsize=(8,7))
    txt3.config(bg=color)
    txt4.config(bg=colorpunktow)
    global grubosc
    global style
    if cb1.current()!=None:
        s= cb1['values'][cb1.current()]
        if s== 'brak':
            style= 'None'
        else:
            style =s

    if cb.current()!=None:
        grubosc = int(cb.current())+1
    plt.title('Położenie wielokąta i punktów', font='Arial', fontsize='20')

    if(cb2.current()==0):
        plt.scatter(pkty, pktx, marker='o',color=colorpunktow)
        plt.scatter(xd, yd, marker='o', color=colorpunktow)
    plt.plot(Xk, Yk, color=color, linewidth=grubosc, linestyle=style)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, padx=15, pady=15)
    canvas.draw()
def wykres1(grubosc):
    fig = plt.figure(figsize=(8,7))
    txt3.config(bg=color)
    txt4.config(bg=colorpunktow)
    if cb2.current()==0:
        plt.scatter(pkty, pktx, marker='o',color=colorpunktow)
        plt.scatter(xd, yd, marker='o', color=colorpunktow)

    if cb.current()!=None:
        grubosc = int(cb.current())+1
    global style
    if cb1.current()!=None:
        s= cb1['values'][cb1.current()]
        if s== 'brak':
            style= 'None'
        else:
            style =s
    plt.title('Położenie wielokąta i punktów', font='Arial', fontsize='20')
    plt.plot(Xk, Yk, color=color, linewidth=grubosc, linestyle=style)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, padx=15, pady=15)
    canvas.draw()

def dodaj():
    txt5.delete(0,END)
    dod_punkty.append([float(txt2.get()),float(txt1.get())])
    wektory = []
    pkt= []
    angle= []
    print(punkciki)
    fig = plt.figure(figsize=(8, 7))
    plt.title('Położenie wielokąta i punktów', font='Arial', fontsize='20')
    global xd,yd
    for i in range(len(punkciki)):
        a1 = [float(punkciki[i][0]), float(punkciki[i][1])]
        w1 = [float(a1[0]) - float(txt1.get()), float(a1[1]) - float(txt2.get())]
        wektory.append(w1)
        if a1[0] == float(txt2.get()) and a1[1] == float(txt1.get()):
            pkt.append([float(txt2.get()),float(txt1.get())])
            break
    for t in range(len(wektory) - 1):
        angle.append(np.arctan2(wektory[t][0], wektory[t][1]) - np.arctan2(wektory[t + 1][0], wektory[t + 1][1]))

        if angle[t] < -np.pi:
            angle[t] += 2 * np.pi
        if angle[t] > np.pi:
            angle[t] -= 2 * np.pi

    angle = rad2deg(angle)

    s = sum(angle)

    if abs(s) >= 359.999 and abs(s) <= 360.001:
         s = 360
         txt5.insert(0, "Należy do wielokąta")

    else:
        txt5.insert(0,"Nie należy do wielokąta")
    xd.append(float(txt2.get()))
    yd.append(float(txt1.get()))
    txt2.delete(0,END)
    txt1.delete(0,END)
    plt.scatter(xd,yd, marker='o', color=colorpunktow)
    plt.plot(Xk, Yk, color=color)


    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, padx=15, pady=15)
    canvas.draw()

def color_pick():
    global color
    x = colorchooser.askcolor()[1]
    color = x
    wykres()
    return color

#Ramki
frame=LabelFrame(window)
frame.grid(row=0,column=2)

#Buttons

wczytaj= Button(frame, text='Wczytaj dane',height=3, width= 20,command=podzial_punktow)
wczytaj.grid(row=0,column=0)
rysuj= Button(frame, text='Rysuj',height=3, width= 20,command=wykres)
rysuj.grid(row=0,column=1)

dodaj= Button(frame, text='Dodaj punkt',height=3, width= 20, command=dodaj)
dodaj.grid(row=3, column=0, columnspan=2,pady=10)

kolor= Button(frame, text='Wybierz kolor',height=3, width=20, command=color_pick)
kolor.grid(row=4, column=0)

plik= Button(frame, text= 'Wczytaj plik z punktami do sprawdzenia', height=3, width=30, command=wczytaj_punkty)
plik.grid(row=9, column=0,columnspan=2)

kolorpunktow= Button(frame, text='Wybierz kolor punktów',height=3, width=20, command=kolor_punktow)
kolorpunktow.grid(row=8, column=0, pady=15)

liczenie= Button(frame, text='Sprawdź',height=3, width=20, command=lambda:sprawdzam(x,y))
liczenie.grid(row=10, column=0, pady=15, columnspan=2)





#Labels
label= Label(frame, text='Podaj X punktu do analizy',height=3, width=20)
label.grid(row=1, column=0)
label1= Label(frame, text='Podaj Y punktu do analizy',height=3, width=20)
label1.grid(row=2, column=0)
label2= Label(frame, text='Wybierz grubość linii',height=3, width=20)
label2.grid(row=5,column=0)
label3= Label(frame, text='Wybierz styl linii',height=3, width=20)
label3.grid(row=6,column=0)
label4= Label(frame, text='Widoczność punktów',height=3, width=20)
label4.grid(row=7,column=0)
#Entry
txt1= Entry(frame, width=20)
txt1.grid(row=1, column=1, padx=15)
txt2= Entry(frame, width=20)
txt2.grid(row=2, column=1)
txt3= Entry(frame, width=20)
txt3.grid(row=4, column=1)
txt3.config(bg=color)
txt4= Entry(frame, width=20)
txt4.grid(row=8, column=1)
txt4.config(bg=colorpunktow)
txt5= Entry(frame, width=50)
txt5.grid(row=11, column=0, columnspan=2)
txt6= Entry(frame, width=50)
txt6.grid(row=12, column=0, columnspan=2)

var=StringVar()
wart=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cb= ttk.Combobox(frame, textvariable=var)
cb['values']= wart
cb['state']= 'readonly'
cb.current(0)
cb.bind("<<ComboboxSelected>>",wykres1)
cb.grid(column=1, row=5)


var1=StringVar()
wart1=['-','--','-.',':','brak']
cb1= ttk.Combobox(frame, textvariable=var1)
cb1['values']= wart1
cb1['state']= 'readonly'
cb1.current(0)
cb1.bind("<<ComboboxSelected>>",wykres1)
cb1.grid(column=1, row=6)

var2=StringVar()
wart2=['Tak','Nie']
cb2= ttk.Combobox(frame, textvariable=var2)
cb2['values']= wart2
cb2['state']= 'readonly'
cb2.current(0)
cb2.bind("<<ComboboxSelected>>", wykres1)
cb2.grid(column=1, row=7)


window.mainloop()

