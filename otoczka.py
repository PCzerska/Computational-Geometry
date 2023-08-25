from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog
from tkinter import colorchooser
from math import sqrt,degrees,atan2,radians,pi

#wielokat
punkty=[]
points=[]
color='blue'
colorotoczki='#BA55D3'
grubosc=1
style= 'solid'
Yk=[]
Xk=[]

#Chwilowe zamiast otoczki
gorne=[]
dolne=[]
x=[]
y=[]
window = Tk()
window.title("Paulina Czerska GI")
window.geometry('1300x800')
window.configure(background='#87CEFA')


fig=plt.figure(figsize=(8,7))
plt.title('Położenie wielokąta i punktów',)
plt.xticks(np.arange(0,100,10))
plt.yticks(np.arange(0,100,10))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=0, column=0,rowspan=5, padx=15, pady=15)
canvas.draw()


def wczytaj_dane():
    file = filedialog.askopenfilename()
    f = open(file, "r").read()
    lines = f.split('\n')
    global punkciki
    punkty= []
    for line in lines:
        if line != '':
            line=line.split('      ')
            punkty.append(line)

    punkciki=punkty
    return punkciki



def podzial_punktow():
    wczytaj_dane()
    global Yk, Xk,points
    Y= []
    X= []
    for ev in punkciki:
        Y.append(float(ev[0]))
        X.append(float(ev[1]))
    points= np.column_stack((X, Y))

    Yk= Y
    Xk= X


    return Yk,Xk,points

def wykres():
    fig = plt.figure(figsize=(8,7))
    txt1.config(bg=color)
    txt2.config(bg=colorotoczki)
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
        plt.scatter(Xk, Yk, color=color)
    if(cb3.current()==0):
        plt.plot(x,y,linewidth=grubosc,linestyle=style,color=colorotoczki)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, padx=15, pady=15)
    canvas.draw()

def wykres1(grubosc):
    fig = plt.figure(figsize=(8,7))
    txt1.config(bg=color)
    txt2.config(bg=colorotoczki)
    if cb2.current()==0:
        plt.scatter(Xk, Yk, color=color)
    if cb.current()!=None:
        grubosc = int(cb.current())+1

    global style
    if cb1.current() != None:
        s = cb1['values'][cb1.current()]
        if s == 'brak':
            style = 'None'
        else:
            style = s

    if (cb3.current() == 0):
        plt.plot(x, y, linewidth=grubosc,linestyle=style, color=colorotoczki)

    plt.title('Położenie wielokąta i punktów', font='Arial', fontsize='20')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, padx=15, pady=15)
    canvas.draw()

def color_pick():
    global color
    x = colorchooser.askcolor()[1]
    color = x
    wykres()
    return color

def kolor_otoczki():
    global colorotoczki
    x = colorchooser.askcolor()[1]
    colorotoczki = x
    txt2.config(bg=str(colorotoczki))
    wykres1(grubosc)
    return colorotoczki

def od_nowa():
    global punkty,Yk,Xk,color,colorotoczki,grubosc,style,x,y
    x=[]
    y=[]
    punkty = []
    Yk = []
    Xk = []
    color='blue'
    colorotoczki='#BA55D3'
    grubosc=1
    style= 'solid'
    cb.current(0)
    cb1.current(0)
    cb2.current(0)
    cb3.current(0)
    txt1.config(bg=color)
    txt2.config(bg=colorotoczki)
    podzial_punktow()
    fig = plt.figure(figsize=(8, 7))
    plt.title('Położenie wielokąta i punktów', font='Arial', fontsize='20')
    plt.xticks(np.arange(0, 100, 10))
    plt.yticks(np.arange(0, 100, 10))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=5, padx=15, pady=15)
    canvas.draw()


def orientation(p, q, r):
    #Funkcja oblicza iloczyn skalarny wektorów p-q i q-r,
    #jeśli jest on większy od zera oznacza to lewą orientację,
    #jeśli jest mniejszy oznacza to prawą orientację.
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def max_left(points):
    #Znajdywanie skrajnego lewego punktu
    left = min(points[:, 1])
    minm = max(points[:, 0])
    minimalne_idx = 0
    for i in range(len(points)):
        if left == points[i][1] and points[i][0] < minm:
            minimalne_idx = i
    return minimalne_idx


def otoczka():
    global points,x,y
    otoczka = []
    nast = 0
    n= len(points)
    left= max_left(points)
    current= left
    while nast != left:
        nast = (current + 1) % n
        otoczka.append(current)
        for i in range(n):
            if (i != current and i != nast):
                if orientation(points[current], points[i], points[nast]) == 2:
                    nast= i
        current= nast
    x= []
    y= []
    for idx in otoczka:
        x.append(points[idx][0])
        y.append(points[idx][1])
        points[idx] = None
    otoczka_points= np.column_stack((x, y))
    otoczka_points= np.append(otoczka_points, np.array([otoczka_points[0]]), axis=0)
    x.append(x[0])
    y.append(y[0])
    print(x,y)
    wykres()
    return otoczka_points, points








#Ramki
frame=LabelFrame(window)
frame.grid(row=0,column=2)

#Labels
label1= Label(frame, text='Wybierz grubość linii',height=3, width=20)
label1.grid(row=3,column=0)
label2= Label(frame, text='Wybierz styl linii',height=3, width=20)
label2.grid(row=4,column=0)
label3= Label(frame, text='Widoczność punktów',height=3, width=20)
label3.grid(row=5,column=0)
label4= Label(frame, text='Widoczność otoczki',height=3, width=20)
label4.grid(row=6,column=0)
#Buttons
wczytaj= Button(frame, text='Wczytaj dane',height=3, width= 20,command=podzial_punktow)
wczytaj.grid(row=0,column=0)

rysuj= Button(frame, text='Rysuj',height=3, width= 20,command=wykres)
rysuj.grid(row=0,column=1)

kolor= Button(frame, text='Wybierz kolor',height=3, width=20, command=color_pick)
kolor.grid(row=1, column=0)

kolorotoczki= Button(frame, text='Wybierz kolor otoczki',height=3, width=20, command=kolor_otoczki)
kolorotoczki.grid(row=2, column=0)

nowe= Button(frame, text='Zacznij od nowa',height=3, width=20, command=od_nowa)
nowe.grid(row=7,column=0,columnspan=2)

otoczka= Button(frame, text='Otoczka',height=3, width=20, command= otoczka)
otoczka.grid(row=8,column=0,columnspan=2)
#Entry
txt1= Entry(frame, width=20)
txt1.grid(row=1, column=1)
txt1.config(bg=color)

txt2= Entry(frame, width=20)
txt2.grid(row=2, column=1)
txt2.config(bg=colorotoczki)

#Comboboxxy
var= StringVar()
wart=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
cb= ttk.Combobox(frame, textvariable=var)
cb['values']= wart
cb['state']= 'readonly'
cb.current(0)
cb.bind("<<ComboboxSelected>>",wykres1)
cb.grid(column=1, row=3)

var1=StringVar()
wart1=['-','--','-.',':','brak']
cb1= ttk.Combobox(frame, textvariable=var1)
cb1['values']= wart1
cb1['state']= 'readonly'
cb1.current(0)
cb1.bind("<<ComboboxSelected>>",wykres1)
cb1.grid(column=1, row=4)

var2=StringVar()
wart2=['Tak','Nie']
cb2= ttk.Combobox(frame, textvariable=var2)
cb2['values']= wart2
cb2['state']= 'readonly'
cb2.current(0)
cb2.bind("<<ComboboxSelected>>", wykres1)
cb2.grid(column=1, row=5)

var3=StringVar()
wart3=['Tak','Nie']
cb3= ttk.Combobox(frame, textvariable=var3)
cb3['values']= wart3
cb3['state']= 'readonly'
cb3.current(0)
cb3.bind("<<ComboboxSelected>>", wykres1)
cb3.grid(column=1, row=6)

window.mainloop()

