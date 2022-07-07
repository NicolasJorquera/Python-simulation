
from numpy import pad, random
import numpy as np 

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def greatestInt(array):
    greatest = -1
    for index in range(0, len(array)):
        value = array[index]
        if value > greatest:
            greatest = value
    return greatest        

def plotConcurrencia(isBase, meanVisitas, devVisitas, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, 
duracionPrueba, limiteConcurrencia, limiteCola):

    if isBase:
        
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

        stepCount = 0
        steps = []
        steps = [meanLlegadas1.get(), meanLlegadas2.get(), meanLlegadas3.get(), meanLlegadas4.get(), meanLlegadas5.get(), meanLlegadas6.get(), meanLlegadas7.get()]
        for step in steps:
            if step == "":
                break
            stepCount = stepCount + 1

        stepsTime = []
        stepsTotalTime = 0
        for step in range(stepCount):
            stepsTotalTime = stepsTotalTime + round(int(duracionPrueba.get())/stepCount)
            stepsTime.append(round(int(duracionPrueba.get())/stepCount))
        
        while stepsTotalTime != int(duracionPrueba.get()):
            if stepsTotalTime > int(duracionPrueba.get()):
                stepsTime[-1] = stepsTime[-1] - 1
                stepsTotalTime = stepsTotalTime -1
            else:
                stepsTime[-1] = stepsTime[-1] + 1
                stepsTotalTime = stepsTotalTime +1

        tiempoTotal = 0
        for stepIndex in range(stepCount):
        
            segundo = 0
            size = random.poisson(lam=int(steps[stepIndex]), size=1)
            while size < 0:
                size = random.poisson(lam=int(steps[stepIndex]), size=1)
            while segundo < stepsTime[stepIndex] or (stepIndex == stepCount-1 and segundo >= stepsTime[stepIndex] and (cola != [] or concurrencia != [])):

                if segundo <  stepsTime[stepIndex]:
                    size = random.poisson(lam=int(steps[stepIndex]), size=1)
                    while size < 0:
                        size = random.poisson(lam=int(steps[stepIndex]), size=1)
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

                # for cola2Index in range(0, len(cola2)):
                #     cola2[cola2Index]["tiempoRespuesta"] = cola2[cola2Index]["tiempoRespuesta"] + 1


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
                        tiempoRespuesta.append(int(meanVisitas.get()))
                
                segundo = segundo + 1
            tiempoTotal = tiempoTotal + segundo
        
        if len(poissonData) > 0:
            arriveX = greatestInt(poissonData)
            arriveY = [0] * (arriveX + 1)
            for arrivalsIndex in range(0, len(poissonData)):
                arrivals = poissonData[arrivalsIndex]
                arriveY[arrivals] = arriveY[arrivals] + 1
            
            for item in range(0, len(arriveY)):
                arriveY[item] = (float(arriveY[item])/float(len(poissonData)))


        return range(tiempoTotal), concurrenciaTotal, colaTotal, cola2Total, tiempoRespuesta, range(arriveX + 1), arriveY, poissonData, visitasFinalizadas
    
    else:
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

        llegadas = meanLlegadas1

        tiempoTotal = 0
        
        segundo = 0
        while segundo < len(llegadas) or cola != [] or concurrencia != []:

            if segundo <  len(llegadas):
                poissonData.append(llegadas[segundo])
                for visita in range(llegadas[segundo]):
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

            # for cola2Index in range(0, len(cola2)):
            #     cola2[cola2Index]["tiempoRespuesta"] = cola2[cola2Index]["tiempoRespuesta"] + 1


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
                    tiempoRespuesta.append(int(meanVisitas.get()))
            
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


def rendimiento(tiempo, llegadas, finalizadas, rendStep):
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