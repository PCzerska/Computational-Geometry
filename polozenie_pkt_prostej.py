from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
cp1='#fcba03'
cp2='#2039ba'

window = Tk()
window.title("Form 1")
window.geometry('1350x900')

fig=plt.figure()
plt.xticks(np.arange(0,100,10))
plt.yticks(np.arange(0,100,10))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(row=0, column=6, rowspan=7, pady=20, padx=60)
canvas.draw()

lbl1 = Label(window, text='Xa:', font=20, padx=30)
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text='Ya:', font=20, padx=30)
lbl2.grid(column=3, row=0)
lbl3 = Label(window, text='Xb:', font=20)
lbl3.grid(column=0, row=1)
lbl4 = Label(window, text='Yb:', font=20)
lbl4.grid(column=3, row=1)
lbl5 = Label(window, text='Xc:', font=20)
lbl5.grid(column=0, row=2)
lbl6 = Label(window, text='Yc:', font=20)
lbl6.grid(column=3, row=2)
lbl7 = Label(window, text='Xd:', font=20)
lbl7.grid(column=0, row=3)
lbl8 = Label(window, text='Yd:', font=20)
lbl8.grid(column=3, row=3)
lbl9 = Label(window, text='Xp:', font=20)
lbl9.grid(column=0, row=5)
lbl10 = Label(window, text='Yp:', font=20)
lbl10.grid(column=3, row=5)
lbl11 = Label(window, text= 'Wybierz grubość pierwszej linii:')
lbl11.grid(column=0, row=9,columnspan=3)
lbl12 = Label(window, text= 'Wybierz grubość drugiej linii:')
lbl12.grid(column=0, row=10,columnspan=3)
lbl13 = Label(window, text= 'Widoczność oznaczeń:')
lbl13.grid(column=0, row=11, columnspan=3)
lbl14 = Label(window, text= 'Wybierz styl linii pierwszej:')
lbl14.grid(column=0, row=12, columnspan=3)
lbl15 = Label(window, text= 'Wybierz styl drugiej:')
lbl15.grid(column=0, row=13, columnspan=3)
# lbl15 = Label(window, text= 'Aby zmienić kolor, grubość i widoczność,\n najpierw wybierz parametry,\n a następnie kliknij "Rysuj"\n')
# lbl15.grid(column=0, row=10,columnspan=6, rowspan=5)

var= StringVar()
var1= StringVar()
var2= StringVar()
var3= StringVar()
var4= StringVar()
wart=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
wart1= ['Tak', 'Nie']
wart2= ["solid", "dashdot", "dotted", "dashed","None"]
cb= ttk.Combobox(window, textvariable=var)
cb['values']= wart
cb['state']= 'readonly'
cb.grid(column=3, row=9)
cb1= ttk.Combobox(window, textvariable=var1)
cb1['values']= wart
cb1['state']= 'readonly'
cb1.grid(column=3, row=10)
cb2= ttk.Combobox(window, textvariable=var2)
cb2['values']= wart1
cb2['state']= 'readonly'
cb2.grid(column=3, row=11)
cb3= ttk.Combobox(window, textvariable=var3)
cb3['values']=wart2
cb3['state']='readonly'
cb3.grid(column=3, row=12)
cb4= ttk.Combobox(window, textvariable=var4)
cb4['values']=wart2
cb4['state']='readonly'
cb4.grid(column=3, row=13)

space = Label(window, text='  ')
space.grid(column=2, row=0)

txt1 = Entry(window, width=20)
txt1.grid(column=1, row=0)
txt2 = Entry(window, width=20)
txt2.grid(column=4, row=0)
txt3 = Entry(window, width=20)
txt3.grid(column=1, row=1)
txt4 = Entry(window, width=20)
txt4.grid(column=4, row=1)
txt5 = Entry(window, width=20)
txt5.grid(column=1, row=2)
txt6 = Entry(window, width=20)
txt6.grid(column=4, row=2)
txt7 = Entry(window, width=20)
txt7.grid(column=1, row=3)
txt8 = Entry(window, width=20)
txt8.grid(column=4, row=3)
txt9 = Entry(window, width=20)
txt9.grid(column=1, row=5)
txt10 = Entry(window, width=20)
txt10.grid(column=4, row=5)
txt11= Entry(window, width=100)
txt11.grid(column=6, row=14, columnspan=3)

labels=[txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10]


def color1(x):
    global cp1
    x= colorchooser.askcolor()[1]
    cp1=x
    return cp1

def color2(x):
    global cp2
    x= colorchooser.askcolor()[1]
    cp2=x
    return cp2

def widocznosc():
    inf= cb2.current()
    return inf

def pobierz_dane():
    yA = float(txt1.get())
    xA = float(txt2.get())
    yB = float(txt3.get())
    xB = float(txt4.get())
    yC = float(txt5.get())
    xC = float(txt6.get())
    yD = float(txt7.get())
    xD = float(txt8.get())
    return yA, xA, yB, xB, yC, xC, yD, xD
def obld(xA, yA, xB, yB, xC, yC, xD, yD):
    xab = xB - xA
    yab = yB - yA
    xcd = xD - xC
    ycd = yD - yC
    xac = xC - xA
    yac = yC - yA
    return xab,yab,xcd,ycd,xac,yac

def oblt(xab, yab, xcd, ycd, xac, yac, xA, yA):

    if ((xab * ycd - yab * xcd) == 0):
        return "Proste są równoległe lub się pokrywają"
    t1 = (xac * ycd - yac * xcd) / (xab * ycd - yab * xcd)
    xP = xA + t1 * xab
    yP = yA + t1 * yab
    return xP, yP

def szer1():
    szer= int(cb.current())
    return szer
def szer2():
    szer= int(cb1.current())
    return szer

def style():
    s= cb3.current()
    return s

def style1():
    s= cb4.current()
    return s


def clicked():
    yA, xA, yB, xB, yC, xC, yD, xD = pobierz_dane()
    xab, yab, xcd, ycd, xac, yac = obld(xA, yA, xB, yB, xC, yC, xD, yD)


    if ((xab * ycd - yab * xcd) != 0):
        t1 = (xac * ycd - yac * xcd) / (xab * ycd - yab * xcd)
        t2 = (xac * yab - yac * xab) / (xab * ycd - yab * xcd)
        odp=kons()
        txt11.insert(0,odp)
        xP, yP= oblt(xab,yab,xcd,ycd,xac,yac,xA,yA)
        xP= round(xP,4)
        yP= round(yP,4)
        txt9.insert(0,yP)
        txt10.insert(0,xP)
        # wstawianie płótna
        fig = plt.figure()
        Xab, Yab= [xA, xB], [yA, yB]
        Xcd, Ycd= [xC, xD], [yC, yD]
        s1= szer1()
        s2= szer2()
        plt.plot(Xab,Yab,marker='s', color= cp1, linewidth= s1)
        plt.plot(Xcd,Ycd, marker='s', color= cp2, linewidth= s2)
        plt.plot(xP, yP, marker='s')
        plt.annotate('A',(xA,yA), size= 15)
        plt.annotate('B',(xB,yB), size= 15)
        plt.annotate('C',(xC,yC), size= 15)
        plt.annotate('D',(xD,yD), size= 15)
        plt.annotate('P',(xP,yP), size= 15)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=7)
        frame = Frame(window)
        frame.grid(row=11, column=6, rowspan=10)
        NavigationToolbar2Tk(canvas, frame)
        canvas.draw()


        return xP, yP
    else:
        w=oblt(xab,yab,xcd,ycd,xac,yac,xA,yA)
        txt11.insert(0, w)
        # wstawianie płótna
        fig = plt.figure()
        Xab, Yab = [xA, xB], [yA, yB]
        Xcd, Ycd = [xC, xD], [yC, yD]
        s1 = szer1()
        s2 = szer2()
        plt.plot(Xab, Yab, marker='s', color=cp1, linewidth=s1)
        plt.plot(Xcd, Ycd, marker='s', color=cp2, linewidth=s2)
        plt.annotate('A', (xA, yA), size=15)
        plt.annotate('B', (xB, yB), size=15)
        plt.annotate('C', (xC, yC), size=15)
        plt.annotate('D', (xD, yD), size=15)
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=7)
        frame = Frame(window)
        frame.grid(row=11, column=6, rowspan=10)
        NavigationToolbar2Tk(canvas, frame)
        canvas.draw()







def ofile():
    file= filedialog.askopenfilename()
    f=open(file,"r")
    f=f.read().split(' ')
    txt1.insert(0,f[0])
    txt2.insert(0,f[1])
    txt3.insert(0,f[2])
    txt4.insert(0,f[3])
    txt5.insert(0,f[4])
    txt6.insert(0,f[5])
    txt7.insert(0,f[6])
    txt8.insert(0,f[7])

def zapis():
    f= filedialog.asksaveasfile(initialfile='Bez tytulu.txt', mode= 'w', defaultextension=".txt")
    if f is None:
        return
    data=''
    for i in range(0,len(labels)):
        data+=str(labels[i].get()) + ', '
    f.write(data)
    f.close()
def fun():
    color1(cp1)
def fun2():
    color2(cp2)
def rysowanie():
    yA, xA, yB, xB, yC, xC, yD, xD = pobierz_dane()
    xab, yab, xcd, ycd, xac, yac = obld(xA, yA, xB, yB, xC, yC, xD, yD)
    if ((xab * ycd - yab * xcd) != 0):
        xP, yP = oblt(xab, yab, xcd, ycd, xac, yac, xA, yA)
        xP = round(xP, 4)
        yP = round(yP, 4)
        sz1=szer1()
        sz1+=1
        sz2=szer2()
        sz2+=1
        inf = widocznosc()
        s = int(style())
        s1= int(style1())
        styl = cb3['values'][s]
        styl1 = cb4['values'][s1]

        # wstawianie płótna
        fig = plt.figure()
        Xab, Yab = [xA, xB], [yA, yB]
        Xcd, Ycd = [xC, xD], [yC, yD]
        plt.plot(Xab, Yab,color=cp1, marker='s',linewidth= sz1, ls=styl)
        plt.plot(Xcd, Ycd,color=cp2, marker='s',linewidth= sz2, ls=styl1)
        plt.plot(xP, yP, marker='s')


        if(inf==0):
            plt.annotate('A', (xA, yA), size= 15)
            plt.annotate('B', (xB, yB), size= 15)
            plt.annotate('C', (xC, yC), size= 15)
            plt.annotate('D', (xD, yD), size= 15)
            plt.annotate('P', (xP, yP), size= 15)

        frame=Frame(window)
        frame.grid(row=11, column=6, rowspan=10)
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=7)
        NavigationToolbar2Tk(canvas, frame)
        canvas.draw()
    else:
        sz1 = szer1()
        sz2 = szer2()
        inf = widocznosc()
        s = int(style())
        s1 = int(style1())
        styl = cb3['values'][s]
        styl1 = cb4['values'][s1]
        print(type(styl))
        # wstawianie płótna
        fig = plt.figure()
        Xab, Yab = [xA, xB], [yA, yB]
        Xcd, Ycd = [xC, xD], [yC, yD]
        plt.plot(Xab, Yab, color=cp1, marker='s', linewidth=sz1)
        plt.plot(Xcd, Ycd, color=cp2, marker='s', linewidth=sz2)

        if (inf == 0):
            plt.annotate('A', (xA, yA), size=15)
            plt.annotate('B', (xB, yB), size=15)
            plt.annotate('C', (xC, yC), size=15)
            plt.annotate('D', (xD, yD), size=15)


        frame = Frame(window)
        frame.grid(row=11, column=6, rowspan=10)
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=7)
        NavigationToolbar2Tk(canvas, frame)
        canvas.draw()


def kons():
    yA, xA, yB, xB, yC, xC, yD, xD = pobierz_dane()
    xab, yab, xcd, ycd, xac, yac = obld(xA, yA, xB, yB, xC, yC, xD, yD)
    t1 = (xac * ycd - yac * xcd) / (xab * ycd - yab * xcd)
    t2 = (xac * yab - yac * xab) / (xab * ycd - yab * xcd)
    if ((0 <= t1) and (t1 <= 1) and (0 <= t2) and (t2 <= 1)):
        return("Punkt należy do obu odcinków")
    else:
        return("Odcinki się nie przecinają, ale proste tak")



def zamknij():
    window.destroy()

btno = Button(window, text="Oblicz", height=3, width=20, command= clicked)
btno.grid(column=0, row=4, columnspan=5)
btnt = Button(window, text="Wczytaj dane z pliku", height=3, width=20, command= ofile)
btnt.grid(column=0, row=6, columnspan=3)
btns = Button(window, text="Zapisz dane do pliku", height=3, width=20, command= zapis)
btns.grid(column=3, row=6, columnspan=3)
btncl = Button(window, text="Zamknij", height=3, width=20, command= zamknij)
btncl.grid(column=3, row=5, columnspan=3, rowspan=12)
btnr = Button(window, text="Rysuj", height=3, width=20, command=rysowanie)
btnr.grid(column=0, row=5, columnspan=3, rowspan=12)
btnc = Button(window, text="Zmień kolor pierwszej linii", height=2, width=70, command= fun)
btnc.grid(column=6, row=7, columnspan=3)
btnc1= Button(window, text="Zmień kolor drugiej linii", height=2, width=70, command= fun2)
btnc1.grid(column=6, row=8, columnspan=3, pady=20)

window.mainloop()








