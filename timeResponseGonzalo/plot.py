
import matplotlib.pyplot as plt

import simulacion

def plot(duracionPrueba, tiempoTotal, visitasFinalizadas, bloque, tiempoRespuesta, concurrencia, cola, errores, poissonData, visitas, frecVisitas):
    

    tiempoTotal = range(tiempoTotal)
    fig, (axs1, axs2, axs3) = plt.subplots(3,2)
    fig.canvas.set_window_title('Bloque ' + bloque)

    tiempoRespuestaSinCeros = []
    for tiempo in tiempoRespuesta:
        if tiempo > 0:
            tiempoRespuestaSinCeros.append(tiempo)

    bins = int(max(tiempoRespuestaSinCeros)-min(tiempoRespuestaSinCeros))

    axs1[0].hist(tiempoRespuestaSinCeros, bins)
    axs1[0].set(xlabel='Duracion Visitas', ylabel='Visitas')
    axs1[1].plot(tiempoTotal, concurrencia)
    axs1[1].plot(tiempoTotal, cola)
    axs1[1].plot(tiempoTotal, errores)
    axs1[1].set(xlabel='Tiempo', ylabel='Concurrencia(Azul)/Cola(Naranjo)')
    axs2[0].plot(tiempoTotal, tiempoRespuesta)
    axs2[0].set(xlabel='Tiempo', ylabel='Tiempo de respuesta')
    axs2[1].hist(poissonData, int(round(len(visitas)*0.9, 0)), density=True)
    axs2[1].plot(visitas, frecVisitas, '--')
    axs2[1].axis([0,len(visitas),0,1])
    axs2[1].set(xlabel='Visitas', ylabel='Frecuencia')
    if bloque == "A":
        axs3[0].plot(range(int(duracionPrueba)), poissonData)
    else:
        axs3[0].plot(tiempoTotal, poissonData)
    axs3[0].set(xlabel='Tiempo', ylabel='Llegadas')


    axs3prima = axs3[1].twinx()
    rendStep = 5
    tiempoN, llegadasN, finalizadasN = simulacion.rendimiento(tiempoTotal, poissonData, visitasFinalizadas, rendStep)
    axs3[1].bar(tiempoN, llegadasN, width=int(rendStep)*50)
    axs3[1].bar(tiempoN, finalizadasN, width=int(rendStep)*50)
    diff = []
    for i in range(len(tiempoN)):
        if llegadasN[i] == 0:
            diff.append(100)
        else:
            diff.append(100*finalizadasN[i]/llegadasN[i])
     
    axs3prima.plot(tiempoN, diff, color = 'purple')
    axs3prima.axis([-int(rendStep)*50,tiempoN[-1]+int(rendStep)*50,0,110])
    
    

    return visitasFinalizadas