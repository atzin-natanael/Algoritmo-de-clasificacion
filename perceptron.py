from tkinter import *
from tkinter import Tk, Frame, Button,ttk, messagebox, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot
import numpy as np                 #PACHECO ARELLANO ATZIN NATANAEL
import matplotlib.pyplot as plt
from pylab import *
Ventana =Tk()
Ventana.geometry('900x800')
Ventana.title('Grafica')

Ventana.minsize(width=850, height=750)
frame = Frame(Ventana, bg='blue')
frame.grid(column=0,row=0,sticky='nsew')
# Crear caja de texto.
Ventana.config(width=300, height=200)
entry = ttk.Entry()
entry.place(x=80, y=60)
Ventana.config(width=300, height=200)
entry = ttk.Entry()
entry.place(x=50, y=30)
Ventana.config(width=300, height=200)
entry = ttk.Entry()
entry.place(x=50, y=1)
Label_middle = ttk.Label(Ventana, text='W2: ')
Label_middle.place(x = 30, y = 40,anchor = 'center')
Label_middle = ttk.Label(Ventana, text='UMBRAL: ')
Label_middle.place(x = 30, y = 70,anchor = 'center')
Label_middle = ttk.Label(Ventana, text='W1: ')
Label_middle.place(x = 30, y = 10,anchor = 'center')
#Clasificar
#Puntos en la grafica, variables
xs = []
ys = []
w = [1,1]
umbral = -1.5 #theta
c = umbral / w[1]
m = -w[0] / w[1]
colors = ['k']
#Ancho y largo del plano
xmin, xmax, ymin, ymax = -6, 6, -6, 6
f_cuadros = 1
#Grafica
fig, ax = plt.subplots(figsize=(9, 9))
canvas= FigureCanvasTkAgg(fig,master=frame)
def actualizar():
    ax.scatter(xs, ys, c=colors)
#Escalar valores
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
#Mover la grafica a plano cartesiano
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
# X - Y valores en los ejes (nombre, tamaño, x, y , rotacion)
ax.set_xlabel('X', size=15, labelpad=-24, x=1.02)
ax.set_ylabel('Y', size=15, labelpad=-21, y=1.02, rotation=0)
# Crea determinados valores de cuadricula
x_cuadro = np.arange(xmin, xmax+1, f_cuadros)
y_cuadro = np.arange(ymin, ymax+1, f_cuadros)
ax.set_xticks(x_cuadro[x_cuadro != 0])
ax.set_yticks(y_cuadro[y_cuadro != 0])
#Cuadricula
ax.grid()
plt.subplots_adjust(bottom=0.2)
#Boton --- izquierda, abajo, ancho, altura
def activacion():

    #print(w)
    #print(xs)
    i = 0
    sumaxs=0
    sumays=0
    for i in range(len(xs)):
        print(i, ' punto ', w[i]*xs[i] - umbral)
        if(w[i]*xs[i]+ w[i]*ys[i] - umbral >= 0):
            print("Aceptada")
            ax.scatter(xs[i], ys[i], c='green')

        else:
            print("No aceptada")
            ax.scatter(xs[i], ys[i], c='red')
        sumaxs = xs[i]*w[i]+sumaxs
        sumays= ys[i]*w[i]+sumays
    u= sumaxs+ sumays-umbral
    print(c)
    print('funcion U: ', u)
def f1(x):
    return x*m + c
def clasificar():
    activacion()
    pyplot.plot(xs, [f1(i) for i in xs])
    plt.draw();
    messagebox.showinfo(message="HECHO :)")

boton = ttk.Button(text="Clasificar",command=clasificar)
boton.place(x=415, y=20)

def mouse_event(event):
            #print('x: {} and y: {}'.format(event.xdata, event.ydata))
            xs.append(event.xdata);
            ys.append(event.ydata);
            w.append(1);
            actualizar();
            plt.draw();
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)
canvas.draw()
canvas.get_tk_widget().grid(column=0,row=0,rowspan=1)
try:
    Ventana.mainloop()
except KeyboardInterrupt:
       print("Programa finalizado correctamente")
       raise SystemExit