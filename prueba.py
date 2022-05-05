from math import exp
import tkinter as tk
from tkinter import BOTTOM, CENTER, RIGHT, LEFT, TOP, ttk
from tkinter.messagebox import showinfo
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np 

from numpy import random

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

# root window
root = tk.Tk()
root.geometry("200x400")
root.resizable(False, False)
root.title('Simulador distribucion')

plot = ttk.Frame(root)
plot.pack(padx=10, pady=10, fill='x', side=RIGHT)


inputs = ttk.Frame(root)
inputs.pack(padx=10, pady=10, fill='x', side=LEFT)

general_label = ttk.Label(inputs, text="General:")
general_label.pack(fill='x', side=TOP)
general = ttk.Frame(inputs)
general.pack(padx=10, pady=10, fill='x')


lleg_label = ttk.Label(inputs, text="Llegadas (Poisson):")
lleg_label.pack(fill='x', side=TOP)
llegadas = ttk.Frame(inputs)
llegadas.pack(padx=10, pady=10, fill='x')


durVis_label = ttk.Label(inputs, text="Duracion visitas (Normal):")
durVis_label.pack(fill='x', side=TOP)
duracionVisitas = ttk.Frame(inputs)
duracionVisitas.pack(padx=10, pady=10, fill='x')




duracionPrueba = tk.StringVar()

duracion_label = ttk.Label(general, text="Duracion de prueba:")
duracion_label.pack(fill='x', )

duracion_entry = ttk.Entry(general, textvariable=duracionPrueba)
duracion_entry.pack(fill='x')
duracion_entry.focus()




# store mean address and dev

selectionLlegadas = tk.StringVar()
meanLlegadas = tk.StringVar()

# distribution selection
# dist_label = ttk.Label(llegadas, text="Distribucion de probabilidad:")
# dist_label.pack(fill='x', side=TOP)

# dist_input = ttk.Combobox(llegadas, textvariable=selectionLlegadas)
# dist_input['values'] = ["Poisson", "Normal"]
# dist_input['state'] = 'readonly'
# dist_input.pack(fill='x', )
# dist_input.focus()


# mean
mean_label = ttk.Label(llegadas, text="Promedio de llegadas por segundo:")
mean_label.pack(fill='x', )

mean_entry = ttk.Entry(llegadas, textvariable=meanLlegadas)
mean_entry.pack(fill='x')
mean_entry.focus()

# store mean address and dev
selectionVisitas = tk.StringVar()
meanVisitas = tk.StringVar()
devVisitas = tk.StringVar()


# distribution selection
# dist_label = ttk.Label(duracionVisitas, text="Distribucion de probabilidad:")
# dist_label.pack(fill='x', side=TOP)

# dist_input = ttk.Combobox(duracionVisitas, textvariable=selectionVisitas)
# dist_input['values'] = ["Poisson", "Normal"]
# dist_input['state'] = 'readonly'
# dist_input.pack(fill='x', )
# dist_input.focus()


# mean
mean_label = ttk.Label(duracionVisitas, text="Promedio de duracion de visita:")
mean_label.pack(fill='x', )

mean_entry = ttk.Entry(duracionVisitas, textvariable=meanVisitas)
mean_entry.pack(fill='x', )
mean_entry.focus()

# dev
dev_label = ttk.Label(duracionVisitas, text="Desviación estandar:")
dev_label.pack(fill='x', )

dev_entry = ttk.Entry(duracionVisitas, textvariable=devVisitas)
dev_entry.pack(fill='x', )
dev_entry.focus()

def poissonDist(k, lamb):
    temp = exp(-lamb)*(pow(k,lamb))

    fact = 1
    for i in range(1,k+1):
        fact = fact * i

    return (temp/fact)



def plotVisita():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)

    mu = int(meanVisitas.get())
    dev = int(devVisitas.get())
    size = random.poisson(lam=int(meanLlegadas.get()) * int(duracionPrueba.get()), size=1)
  
    datos = np.random.normal( mu, dev, size) #creando muestra de datos


    concurrencia = []
    concurrenciaTotal = []
    mu = int(meanVisitas.get())
    dev = int(devVisitas.get())
    
    return datos

def plotConcurrencia():
    fig = Figure(figsize = (5, 5),
                 dpi = 100)

    lenConcurrencia = 4500
    concurrencia = []
    cola = []
    concurrenciaTotal = []
    mu = int(meanVisitas.get())
    dev = int(devVisitas.get())

    segundo = 0
    while segundo < int(duracionPrueba.get()) or (segundo >= int(duracionPrueba.get()) and cola != []):
        
            
        segundo= segundo + 1

        if segundo < int(duracionPrueba.get()):

            size = random.poisson(lam=int(meanLlegadas.get()), size=1)
            for visita in range(size[0]):
                tiempoVisita = np.random.normal( mu, dev, 1)
                tiempoVisita = truncate(tiempoVisita[0])
                if len(concurrencia) < lenConcurrencia:
                    concurrencia.append(tiempoVisita)
                else:
                    cola.append(tiempoVisita)

        concurrenciaTotal.append(len(concurrencia))
        
        offset = 0
        for visitaIndex in range(0, len(concurrencia)):
            visitaIndex = visitaIndex - offset
            if int(concurrencia[visitaIndex]) <= 0:
                concurrencia.pop(visitaIndex)
                if len(cola) > 0 and len(concurrencia)<lenConcurrencia:
                    concurrencia.append(cola[0])
                    cola.pop(0)
                else:
                    offset = offset + 1
            else:
                concurrencia[visitaIndex] = concurrencia[visitaIndex] - 1

        


    return range(segundo), concurrenciaTotal


def plot():
    datosV = plotVisita()
    tiempoC, concurrencia = plotConcurrencia()


    fig, axs = plt.subplots(2)

    # plot1 = fig.add_subplot(111)
    # plot2 = fig.add_subplot(112)

    axs[0].hist(datosV, 20)
    axs[1].plot(tiempoC, concurrencia)
    plt.show()




button1 = ttk.Button(inputs, text='Graficar', command= plot)
button1.pack(fill='x')

root.mainloop()
