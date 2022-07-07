import bloqueSimple
import matplotlib.pyplot as plt

def plotBase(duracionPrueba, rendStep, meanVisitas, devVisitas, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, limiteConcurrencia, limiteCola):
    tiempoC, concurrencia, cola, cola2, tiempoRespuesta, visitas, frecVisitas, poissonData, visitasFinalizadas = bloqueSimple.plotConcurrencia(True, meanVisitas, devVisitas, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba, limiteConcurrencia, limiteCola)


    fig, (axs1, axs2, axs3) = plt.subplots(3,2)
    fig.canvas.set_window_title('Bloque A')

    bins = int(max(tiempoRespuesta)-min(tiempoRespuesta))

    axs1[0].hist(tiempoRespuesta, bins)
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
    tiempoN, llegadasN, finalizadasN = bloqueSimple.rendimiento(tiempoC, poissonData, visitasFinalizadas, rendStep)
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
    
    return visitasFinalizadas

def plot(duracionPrueba, rendStep, meanVisitas, devVisitas, llegadas, limiteConcurrencia, limiteCola, bloque):
    tiempoC, concurrencia, cola, cola2, tiempoRespuesta, visitas, frecVisitas, poissonData, visitasFinalizadas = bloqueSimple.plotConcurrencia(False, meanVisitas, devVisitas, llegadas, 0, 0, 0, 0, 0, 0, duracionPrueba, limiteConcurrencia, limiteCola)


    fig, (axs1, axs2, axs3) = plt.subplots(3,2)
    fig.canvas.set_window_title('Bloque ' + bloque)

    bins = int(max(tiempoRespuesta)-min(tiempoRespuesta))

    axs1[0].hist(tiempoRespuesta, bins)
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
    axs3[0].plot(range(int(duracionPrueba)), poissonData)
    axs3[0].set(xlabel='Tiempo', ylabel='Llegadas')


    axs3prima = axs3[1].twinx()
    tiempoN, llegadasN, finalizadasN = bloqueSimple.rendimiento(tiempoC, poissonData, visitasFinalizadas, rendStep)
    axs3[1].bar(tiempoN, llegadasN, width=int(rendStep.get())*50)
    axs3[1].bar(tiempoN, finalizadasN, width=int(rendStep.get())*50)
    diff = []
    for i in range(len(tiempoN)):
        if llegadasN[i] == 0:
            diff.append(100)
        else:
            diff.append(100*finalizadasN[i]/llegadasN[i])
     
    axs3prima.plot(tiempoN, diff, color = 'purple')
    axs3prima.axis([-int(rendStep.get())*50,tiempoN[-1]+int(rendStep.get())*50,0,110])
    
    

    return visitasFinalizadas
    