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
limiteConcurrencia = tk.StringVar()
limiteCola = tk.StringVar()

duracion_label = ttk.Label(general, text="Duracion de prueba:")
duracion_label.pack(fill='x', )
duracion_entry = ttk.Entry(general, textvariable=duracionPrueba)
duracion_entry.pack(fill='x')
duracion_entry.focus()

limConcurrencia_label = ttk.Label(general, text="Limite de concurrencia:")
limConcurrencia_label.pack(fill='x', )
limConcurrencia_entry = ttk.Entry(general, textvariable=limiteConcurrencia)
limConcurrencia_entry.pack(fill='x')
limConcurrencia_entry.focus()

limCola_label = ttk.Label(general, text="Limite de cola:")
limCola_label.pack(fill='x', )
limCola_entry = ttk.Entry(general, textvariable=limiteCola)
limCola_entry.pack(fill='x')
limCola_entry.focus()




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


def greatestInt(array):
    greatest = -1
    for value in range(0, len(array)):
        if value > greatest:
            greatest = value
    return greatest        

def plotVisita():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)

    mu = int(meanVisitas.get())
    dev = int(devVisitas.get())
    size = random.poisson(lam=int(meanLlegadas.get()) * int(duracionPrueba.get()), size=1)
  
    datos = np.random.normal( mu, dev, size) #creando muestra de datos
    
    return datos

def plotConcurrencia():
    fig = Figure(figsize = (5, 5),
                 dpi = 100)



    lenConcurrencia = 40
    lenCola = 60

    concurrencia = []
    cola = []
    cola2 = []
    concurrenciaTotal = []
    colaTotal = []
    cola2Total = []
    tiempoRespuesta = []
    poissonData = []
    mu = int(meanVisitas.get())
    dev = int(devVisitas.get())

    segundo = 0
    while segundo < int(duracionPrueba.get()) or (segundo >= int(duracionPrueba.get()) and cola != []):
        
            
        segundo = segundo + 1

        if segundo < int(duracionPrueba.get()):

            size = random.poisson(lam=int(meanLlegadas.get()), size=1)
            while size < 0:
                size = random.poisson(lam=int(meanLlegadas.get()), size=1)
            poissonData.append(size[0])
            for visita in range(size[0]):
                tiempoVisita = np.random.normal( mu, dev, 1)
                tiempoVisita = truncate(tiempoVisita[0])
                dictConcurrencia = {
                    "tiempoVisita": tiempoVisita,
                    "tiempoRespuesta": 0 #Esto incluye los tiempos de espera
                }
                if len(concurrencia) < int(limiteConcurrencia.get()):
                    concurrencia.append(dictConcurrencia)
                else:
                    if(len(cola) >= int(limiteCola.get())):
                        cola2.append(dictConcurrencia)
                    else:
                        cola.append(dictConcurrencia)

        concurrenciaTotal.append(len(concurrencia))
        colaTotal.append(len(cola))
        cola2Total.append(len(cola2))

        mediaTiempoRespuestaData = [0, 0]


        for colaIndex in range(0, len(cola)):
            cola[colaIndex]["tiempoRespuesta"] = cola[colaIndex]["tiempoRespuesta"] + 1

        for cola2Index in range(0, len(cola2)):
            cola2[cola2Index]["tiempoRespuesta"] = cola2[cola2Index]["tiempoRespuesta"] + 1


        offset = 0
        for visitaIndex in range(0, len(concurrencia)):
            visitaIndex = visitaIndex - offset
            concurrencia[visitaIndex]["tiempoRespuesta"] = concurrencia[visitaIndex]["tiempoRespuesta"] + 1
            if int(concurrencia[visitaIndex]["tiempoVisita"]) <= 0:
                mediaTiempoRespuestaData[0] = mediaTiempoRespuestaData[0] + int(concurrencia[visitaIndex]["tiempoRespuesta"])
                mediaTiempoRespuestaData[1] = mediaTiempoRespuestaData[1] + 1
                concurrencia.pop(visitaIndex)

                if len(cola) > 0 and len(concurrencia) < int(limiteConcurrencia.get()):
                    concurrencia.append(cola[0])
                    cola.pop(0)
                    if len(cola2) > 0 and len(cola) < int(limiteCola.get()):
                        #cola.append(cola2[0])
                        cola2.pop(0) 
                else:
                    offset = offset + 1
            else:
                concurrencia[visitaIndex]["tiempoVisita"] = concurrencia[visitaIndex]["tiempoVisita"] - 1

        if mediaTiempoRespuestaData[1] != 0:
            tiempoRespuesta.append(mediaTiempoRespuestaData[0]/mediaTiempoRespuestaData[1])
        else:
            if len(tiempoRespuesta) != 0:
                tiempoRespuesta.append(tiempoRespuesta[-1])
            else:
                tiempoRespuesta.append(0)
    
    if len(poissonData) > 0:
        arriveX = greatestInt(poissonData)
        arriveY = [0] * arriveX
        for arrivals in range(0, len(poissonData)):
            arriveY[arrivals] = arriveY[arrivals] + 1


    return range(segundo), concurrenciaTotal, colaTotal, cola2Total, tiempoRespuesta, range(arriveX), arriveY


def plot():
    datosV = plotVisita()
    tiempoC, concurrencia, cola, cola2, tiempoRespuesta, visitas, frecVisitas = plotConcurrencia()


    fig, (axs1, axs2) = plt.subplots(2,2)

    axs1[0].hist(datosV, 20)
    axs1[0].set(xlabel='Duracion Visitas', ylabel='Visitas')
    axs1[1].plot(tiempoC, concurrencia)
    axs1[1].plot(tiempoC, cola)
    axs1[1].plot(tiempoC, cola2)
    axs1[1].set(xlabel='Tiempo', ylabel='Concurrencia(Azul)/Cola(Naranjo)')
    axs2[0].plot(tiempoC, tiempoRespuesta)
    axs2[0].set(xlabel='Tiempo', ylabel='Tiempo de respuesta')
    axs2[1].plot(visitas, frecVisitas)
    axs2[1].set(xlabel='Visitas', ylabel='Frecuencia')
    plt.show()




button1 = ttk.Button(inputs, text='Graficar', command= plot)
button1.pack(fill='x')

root.mainloop()
