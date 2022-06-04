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
root.geometry("200x500")
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




duracionPrueba = tk.StringVar(value="3600")
limiteConcurrencia = tk.StringVar(value="450")
limiteCola = tk.StringVar(value="200")
rendStep = tk.StringVar(value="5")

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

rendStep_label = ttk.Label(general, text="Step rendimiento (min):")
rendStep_label.pack(fill='x', )
rendStep_entry = ttk.Entry(general, textvariable=rendStep)
rendStep_entry.pack(fill='x')
rendStep_entry.focus()




# store mean address and dev

selectionLlegadas = tk.StringVar()
meanLlegadas = tk.StringVar(value="6")
meanLlegadas2 = tk.StringVar(value="6")

# distribution selection
# dist_label = ttk.Label(llegadas, text="Distribucion de probabilidad:")
# dist_label.pack(fill='x', side=TOP)

# dist_input = ttk.Combobox(llegadas, textvariable=selectionLlegadas)
# dist_input['values'] = ["Poisson", "Normal"]
# dist_input['state'] = 'readonly'
# dist_input.pack(fill='x', )
# dist_input.focus()


# mean
mean_label = ttk.Label(llegadas, text="Llegadas por segundo:")
mean_label.pack(fill='x', )

mean_entry = ttk.Entry(llegadas, textvariable=meanLlegadas)
mean_entry.pack(fill='y')
mean_entry.focus()

mean_entry2 = ttk.Entry(llegadas, textvariable=meanLlegadas2)
mean_entry2.pack(fill='y')
mean_entry2.focus()

# store mean address and dev
selectionVisitas = tk.StringVar()
meanVisitas = tk.StringVar(value="60")
devVisitas = tk.StringVar(value="7")


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
    for index in range(0, len(array)):
        value = array[index]
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
    visitasFinalizadas = []
    mu = int(meanVisitas.get())
    dev = int(devVisitas.get())

    segundo = 0
    size = random.poisson(lam=int(meanLlegadas.get()), size=1)
    while size < 0:
        size = random.poisson(lam=int(meanLlegadas.get()), size=1)
    while segundo < int(duracionPrueba.get()) or (segundo >= int(duracionPrueba.get()) and (cola != [] or concurrencia != [])):

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
        vf = 0
        for visitaIndex in range(0, len(concurrencia)):
            visitaIndex = visitaIndex - offset
            concurrencia[visitaIndex]["tiempoRespuesta"] = concurrencia[visitaIndex]["tiempoRespuesta"] + 1
            if int(concurrencia[visitaIndex]["tiempoVisita"]) <= 0:
                mediaTiempoRespuestaData[0] = mediaTiempoRespuestaData[0] + int(concurrencia[visitaIndex]["tiempoRespuesta"])
                mediaTiempoRespuestaData[1] = mediaTiempoRespuestaData[1] + 1

                
                vf = vf + 1
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
        
        visitasFinalizadas.append(vf) 

        if mediaTiempoRespuestaData[1] != 0:
            tiempoRespuesta.append(mediaTiempoRespuestaData[0]/mediaTiempoRespuestaData[1])
        else:
            if len(tiempoRespuesta) != 0:
                tiempoRespuesta.append(tiempoRespuesta[-1])
            else:
                tiempoRespuesta.append(0)
        
        segundo = segundo + 1
    
    if len(poissonData) > 0:
        arriveX = greatestInt(poissonData)
        arriveY = [0] * (arriveX + 1)
        for arrivalsIndex in range(0, len(poissonData)):
            arrivals = poissonData[arrivalsIndex]
            arriveY[arrivals] = arriveY[arrivals] + 1
        
        for item in range(0, len(arriveY)):
            arriveY[item] = (float(arriveY[item])/float(len(poissonData)))


    return range(segundo), concurrenciaTotal, colaTotal, cola2Total, tiempoRespuesta, range(arriveX + 1), arriveY, poissonData, visitasFinalizadas


def rendimiento(tiempo, llegadas, finalizadas):
    tiempoNuevo = []
    llegadasNuevo = []
    finalizadasNuevo = []
    for segundo in tiempo:
        if segundo == 0:
            tiempoNuevo.append(segundo)
            llegadasNuevo.append(llegadas[segundo])
            finalizadasNuevo.append(finalizadas[segundo])
        else:
            if segundo >= len(llegadas):
                llegadas.append(0)

            step = int(rendStep.get())*60
            if (segundo) % step == 0:
                tiempoNuevo.append(segundo)
                llegadasNuevo.append(llegadas[segundo])
                finalizadasNuevo.append(finalizadas[segundo])
            else:
                llegadasNuevo[-1] = llegadasNuevo[-1] + llegadas[segundo] 
                finalizadasNuevo[-1] = finalizadasNuevo[-1] + finalizadas[segundo] 
    
    return tiempoNuevo, llegadasNuevo, finalizadasNuevo


def plot():
    datosV = plotVisita()
    tiempoC, concurrencia, cola, cola2, tiempoRespuesta, visitas, frecVisitas, poissonData, visitasFinalizadas = plotConcurrencia()

    tiempoRespuesta2 = []
    for item in tiempoRespuesta:
        if item > 0:
            tiempoRespuesta2.append(item)


    fig, (axs1, axs2, axs3) = plt.subplots(3,2)

    bins = int(max(tiempoRespuesta2)-min(tiempoRespuesta2))

    axs1[0].hist(tiempoRespuesta2, bins)
    axs1[0].set(xlabel='Duracion Visitas', ylabel='Visitas')
    axs1[1].plot(tiempoC, concurrencia)
    axs1[1].plot(tiempoC, cola)
    axs1[1].plot(tiempoC, cola2)
    axs1[1].set(xlabel='Tiempo', ylabel='Concurrencia(Azul)/Cola(Naranjo)')
    axs2[0].plot(tiempoC, tiempoRespuesta)
    axs2[0].set(xlabel='Tiempo', ylabel='Tiempo de respuesta')
    axs2[1].hist(poissonData, int(round(len(visitas)*0.9, 0)), density=True)
    axs2[1].plot(visitas, frecVisitas, '--')
    axs2[1].axis([0,len(visitas),0,1])
    axs2[1].set(xlabel='Visitas', ylabel='Frecuencia')
    axs3[0].plot(range(int(duracionPrueba.get())), poissonData)
    axs3[0].set(xlabel='Tiempo', ylabel='Llegadas')


    axs3prima = axs3[1].twinx()
    tiempoN, llegadasN, finalizadasN = rendimiento(tiempoC, poissonData, visitasFinalizadas)
    axs3[1].bar(tiempoN, llegadasN, width=int(rendStep.get())*50)
    axs3[1].bar(tiempoN, finalizadasN, width=int(rendStep.get())*50)
    diff = []
    for i in range(len(tiempoN)):
        if llegadasN[i] == 0:
            diff.append(100);
        else:
            diff.append(100*finalizadasN[i]/llegadasN[i])
     
    axs3prima.plot(tiempoN, diff, color = 'purple')
    axs3prima.axis([-int(rendStep.get())*50,tiempoN[-1]+int(rendStep.get())*50,0,110])
    
    plt.show()




button1 = ttk.Button(inputs, text='Graficar', command= plot)
button1.pack(fill='x')

root.mainloop()
