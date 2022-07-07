
import tkinter as tk
from tkinter import BOTTOM, CENTER, RIGHT, LEFT, TOP, ttk

import numpy as np 

import plot

from numpy import pad, random
import matplotlib.pyplot as plt


# root window
root = tk.Tk()
root.geometry("850x500")
root.resizable(False, False)
root.title('Simulador distribucion')

plot1 = ttk.Frame(root)
plot1.pack(padx=10, pady=10, fill='x', side=RIGHT)


inputs = ttk.Frame(root)
inputs.pack(padx=10, pady=10, fill='y', side=LEFT)

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
meanLlegadas1 = tk.StringVar(value="4")
meanLlegadas2 = tk.StringVar(value="6")
meanLlegadas3 = tk.StringVar(value="8")
meanLlegadas4 = tk.StringVar(value="10")
meanLlegadas5 = tk.StringVar(value="12")
meanLlegadas6 = tk.StringVar(value="14")
meanLlegadas7 = tk.StringVar(value="16")

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

mean_entry1 = ttk.Entry(llegadas, textvariable=meanLlegadas1, width=2)
mean_entry1.pack(side="left", padx=1)
mean_entry1.focus()

mean_entry2 = ttk.Entry(llegadas, textvariable=meanLlegadas2, width=2)
mean_entry2.pack(side="left", padx=1)
mean_entry2.focus()

mean_entry3 = ttk.Entry(llegadas, textvariable=meanLlegadas3, width=2)
mean_entry3.pack(side="left", padx=1)
mean_entry3.focus()

mean_entry4 = ttk.Entry(llegadas, textvariable=meanLlegadas4, width=2)
mean_entry4.pack(side="left", padx=1)
mean_entry4.focus()

mean_entry5 = ttk.Entry(llegadas, textvariable=meanLlegadas5, width=2)
mean_entry5.pack(side="left", padx=1)
mean_entry5.focus()

mean_entry6 = ttk.Entry(llegadas, textvariable=meanLlegadas6, width=2)
mean_entry6.pack(side="left", padx=1)
mean_entry6.focus()

mean_entry7 = ttk.Entry(llegadas, textvariable=meanLlegadas7, width=2)
mean_entry7.pack(side="left", padx=1)
mean_entry7.focus()



# store mean address and dev
selectionVisitas = tk.StringVar()
meanVisitas = tk.StringVar(value="60")
devVisitas = tk.StringVar(value="7")



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









 #### dist #####

distinputs = ttk.Frame(root)
distinputs.pack(padx=10, pady=10, fill='y', side=LEFT)

distgeneral_label = ttk.Label(distinputs, text="Porcentaje:")
distgeneral_label.pack(fill='x', side=TOP)
distgeneral = ttk.Frame(distinputs)
distgeneral.pack(padx=10, pady=10, fill='x')

dist1 = tk.StringVar(value="100")
distInput = ttk.Entry(distinputs, textvariable=dist1)
distInput.pack(fill='x', )
distInput.focus()

distInfo = dist1.get()








inputs2 = ttk.Frame(root)
inputs2.pack(padx=10, pady=10, fill='y', side=LEFT)

general_label2 = ttk.Label(inputs2, text="General:")
general_label2.pack(fill='x', side=TOP)
general2 = ttk.Frame(inputs2)
general2.pack(padx=10, pady=10, fill='x')


durVis_label2 = ttk.Label(inputs2, text="Duracion visitas (Normal):")
durVis_label2.pack(fill='x', side=TOP)
duracionVisitas2 = ttk.Frame(inputs2)
duracionVisitas2.pack(padx=10, pady=10, fill='x')



limiteConcurrencia2 = tk.StringVar(value="100")
limiteCola2 = tk.StringVar(value="50")
rendStep2 = tk.StringVar(value="5")


limConcurrencia_label2 = ttk.Label(general2, text="Limite de concurrencia:")
limConcurrencia_label2.pack(fill='x', )
limConcurrencia_entry2 = ttk.Entry(general2, textvariable=limiteConcurrencia2)
limConcurrencia_entry2.pack(fill='x')
limConcurrencia_entry2.focus()

limCola_label2 = ttk.Label(general2, text="Limite de cola:")
limCola_label2.pack(fill='x', )
limCola_entry2 = ttk.Entry(general2, textvariable=limiteCola2)
limCola_entry2.pack(fill='x')
limCola_entry2.focus()

rendStep_label2 = ttk.Label(general2, text="Step rendimiento (min):")
rendStep_label2.pack(fill='x', )
rendStep_entry2 = ttk.Entry(general2, textvariable=rendStep2)
rendStep_entry2.pack(fill='x')
rendStep_entry2.focus()


meanVisitas2 = tk.StringVar(value="20")
devVisitas2 = tk.StringVar(value="5")

# mean
mean_label2 = ttk.Label(duracionVisitas2, text="Duracion de visita:")
mean_label2.pack(fill='x', )

mean_entry2 = ttk.Entry(duracionVisitas2, textvariable=meanVisitas2)
mean_entry2.pack(fill='x', )
mean_entry2.focus()

# dev
dev_label2 = ttk.Label(duracionVisitas2, text="Desviación estandar:")
dev_label2.pack(fill='x', )

dev_entry2 = ttk.Entry(duracionVisitas2, textvariable=devVisitas2)
dev_entry2.pack(fill='x', )
dev_entry2.focus()







 #### dist #####

distinputs2 = ttk.Frame(root)
distinputs2.pack(padx=10, pady=10, fill='y', side=LEFT)

distgeneral_label2 = ttk.Label(distinputs2, text="Porcentaje:")
distgeneral_label2.pack(fill='x', side=TOP)
distgeneral2 = ttk.Frame(distinputs2)
distgeneral2.pack(padx=10, pady=10, fill='x')

dist2 = tk.StringVar(value="100")
distInput2 = ttk.Entry(distinputs2, textvariable=dist2)
distInput2.pack(fill='x', )
distInput2.focus()

distInfo2 = dist2.get()








inputs3 = ttk.Frame(root)
inputs3.pack(padx=10, pady=10, fill='y', side=LEFT)

general_label3 = ttk.Label(inputs3, text="General:")
general_label3.pack(fill='x', side=TOP)
general3 = ttk.Frame(inputs3)
general3.pack(padx=10, pady=10, fill='x')


durVis_label3 = ttk.Label(inputs3, text="Duracion visitas (Normal):")
durVis_label3.pack(fill='x', side=TOP)
duracionVisitas3 = ttk.Frame(inputs3)
duracionVisitas3.pack(padx=10, pady=10, fill='x')



limiteConcurrencia3 = tk.StringVar(value="100")
limiteCola3 = tk.StringVar(value="50")
rendStep3 = tk.StringVar(value="5")


limConcurrencia_label3 = ttk.Label(general3, text="Limite de concurrencia:")
limConcurrencia_label3.pack(fill='x', )
limConcurrencia_entry3 = ttk.Entry(general3, textvariable=limiteConcurrencia3)
limConcurrencia_entry3.pack(fill='x')
limConcurrencia_entry3.focus()

limCola_label3 = ttk.Label(general3, text="Limite de cola:")
limCola_label3.pack(fill='x', )
limCola_entry3 = ttk.Entry(general3, textvariable=limiteCola3)
limCola_entry3.pack(fill='x')
limCola_entry3.focus()

rendStep_label3 = ttk.Label(general3, text="Step rendimiento (min):")
rendStep_label3.pack(fill='x', )
rendStep_entry3 = ttk.Entry(general3, textvariable=rendStep3)
rendStep_entry3.pack(fill='x')
rendStep_entry3.focus()


meanVisitas3 = tk.StringVar(value="20")
devVisitas3 = tk.StringVar(value="5")

# mean
mean_label3 = ttk.Label(duracionVisitas3, text="Duracion de visita:")
mean_label3.pack(fill='x', )

mean_entry3 = ttk.Entry(duracionVisitas3, textvariable=meanVisitas3)
mean_entry3.pack(fill='x', )
mean_entry3.focus()

# dev
dev_label3 = ttk.Label(duracionVisitas3, text="Desviación estandar:")
dev_label3.pack(fill='x', )

dev_entry3 = ttk.Entry(duracionVisitas3, textvariable=devVisitas3)
dev_entry3.pack(fill='x', )
dev_entry3.focus()




def pl():
    finalizadas = plot.plotBase(duracionPrueba, rendStep, meanVisitas, devVisitas, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, limiteConcurrencia, limiteCola)
    
    for segundo in range(len(finalizadas)):
        finalizadas[segundo] = round(finalizadas[segundo]*(int(dist1.get())/100))
    finalizadas2 = plot.plot(len(finalizadas), rendStep2, meanVisitas2, devVisitas2, finalizadas, limiteConcurrencia2, limiteCola2, 'B')
    
    for segundo in range(len(finalizadas2)):
        finalizadas2[segundo] = round(finalizadas2[segundo]*(int(dist2.get())/100))
    plot.plot(len(finalizadas2), rendStep3, meanVisitas3, devVisitas3, finalizadas2, limiteConcurrencia3, limiteCola3, 'C')
    
    plt.show()







button1 = ttk.Button(inputs, text='Graficar', command= pl)
button1.pack(fill='x')

root.mainloop()
