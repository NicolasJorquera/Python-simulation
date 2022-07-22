
from numpy import pad, random
import numpy as np 
import bloque
import plot

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

def arrivalSteps(meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba):

    stepCount = 0
    steps = [meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7]
    for step in steps:
        if step == "":
            break
        stepCount = stepCount + 1

    stepsTime = []
    stepsTotalTime = 0
    for step in range(stepCount):
        stepsTotalTime = stepsTotalTime + round(int(duracionPrueba)/stepCount)
        stepsTime.append(round(int(duracionPrueba)/stepCount))
    
    while stepsTotalTime != int(duracionPrueba):
        if stepsTotalTime > int(duracionPrueba):
            stepsTime[-1] = stepsTime[-1] - 1
            stepsTotalTime = stepsTotalTime -1
        else:
            stepsTime[-1] = stepsTime[-1] + 1
            stepsTotalTime = stepsTotalTime +1
    
    return stepCount, stepsTime, steps

def checkFinish(visitas, errores, erroresA, erroresB, erroresC, concurrenciaA, concurrenciaB, concurrenciaC, colaA, colaB, colaC, visitasFinalizadas, tiempoRespuesta):
    offset = 0
    tiempoRespuestaSuma = {"A":0, "B":0, "C":0}
    tiempoRespuestaCant = 0
    for visitaIndex in range(len(visitas)):
        visitaIndex = visitaIndex - offset
        if visitas[visitaIndex].get("estado A") != None:
            if visitas[visitaIndex]["estado A"] == "Error":
                errores.append(visitas[visitaIndex])
                erroresA[-1] = erroresA[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado A"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado A"] == "Concurrencia":
                concurrenciaA[-1] = concurrenciaA[-1] + 1
            elif visitas[visitaIndex]["estado A"] == "Cola":
                colaA[-1] = colaA[-1] + 1

        if visitas[visitaIndex].get("estado B") != None:
            if visitas[visitaIndex]["estado B"] == "Error":
                errores.append(visitas[visitaIndex])
                erroresA[-1] = erroresA[-1] + 1
                erroresB[-1] = erroresB[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado B"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado B"] == "Concurrencia":
                concurrenciaB[-1] = concurrenciaB[-1] + 1
            elif visitas[visitaIndex]["estado B"] == "Cola":
                colaB[-1] = colaB[-1] + 1
        
        if visitas[visitaIndex].get("estado C") != None:
            if visitas[visitaIndex]["estado C"] == "Error":
                errores.append(visitas[visitaIndex])
                erroresA[-1] = erroresA[-1] + 1
                erroresB[-1] = erroresB[-1] + 1
                erroresC[-1] = erroresC[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue

            elif visitas[visitaIndex]["estado C"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado C"] == "Concurrencia":
                concurrenciaC[-1] = concurrenciaC[-1] + 1
            elif visitas[visitaIndex]["estado C"] == "Cola":
                colaC[-1] = colaC[-1] + 1

            if visitas[visitaIndex]["estado C"] == "Concurrencia, bloque finalizado":
                tiempoRespuestaSuma["A"] =+ visitas[visitaIndex]["tiempoRespuesta A"]
                tiempoRespuestaSuma["B"] =+ visitas[visitaIndex]["tiempoRespuesta B"]
                tiempoRespuestaSuma["C"] =+ visitas[visitaIndex]["tiempoRespuesta C"]
                tiempoRespuestaCant =+ 1

                visitasFinalizadas.append(visitas[visitaIndex])
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
    if tiempoRespuestaCant > 0:
        tiempoRespuesta["A"].append(tiempoRespuestaSuma["A"]/tiempoRespuestaCant)
        tiempoRespuesta["B"].append(tiempoRespuestaSuma["B"]/tiempoRespuestaCant)
        tiempoRespuesta["C"].append(tiempoRespuestaSuma["C"]/tiempoRespuestaCant)
    elif len(visitasFinalizadas) > 0:
        tiempoRespuesta["A"].append(tiempoRespuesta["A"][-1])
        tiempoRespuesta["B"].append(tiempoRespuesta["B"][-1])
        tiempoRespuesta["C"].append(tiempoRespuesta["C"][-1])
    else:
        tiempoRespuesta["A"].append(0)
        tiempoRespuesta["B"].append(0)
        tiempoRespuesta["C"].append(0)

def plotSetUp(duracionPrueba, tiempoTotal, visitasFinalizadas, bloques, tiempoRespuesta, concurrencias, colas, errores, llegadas, arriveX, arriveY):
    
    for letraBloqueIndex in range(len(bloques)):
        plot.plot(duracionPrueba, tiempoTotal,visitasFinalizadas, bloques[letraBloqueIndex], tiempoRespuesta[bloques[letraBloqueIndex]], concurrencias[letraBloqueIndex], colas[letraBloqueIndex], errores[letraBloqueIndex], llegadas[bloques[letraBloqueIndex]], range(arriveX[bloques[letraBloqueIndex]]  + 1), arriveY[bloques[letraBloqueIndex]] )
        
    
def poissonDataArrange(llegadas, arriveX, arriveY):
    for bloque in llegadas:
     
        if len(llegadas[bloque]) > 0:
            arriveX[bloque] = greatestInt(llegadas[bloque])
            arriveY[bloque]  = [0] * (arriveX[bloque] + 1)
            for arrivalsIndex in range(0, len(llegadas[bloque])):
                arrivals = llegadas[bloque][arrivalsIndex]
                arriveY[bloque][arrivals] = arriveY[bloque][arrivals] + 1
            
            for item in range(0, len(arriveY[bloque])):
                arriveY[bloque][item] = (float(arriveY[bloque][item])/float(len(llegadas[bloque])))


def simulacion(info):
    meanVisitas1, devVisitas1, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba, limiteConcurrencia1, limiteCola1 = info[0]
    dist1 = int(info[1])
    meanVisitas2, devVisitas2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia2, limiteCola2 = info[2]
    dist2 = int(info[3])
    meanVisitas3, devVisitas3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia3, limiteCola3 = info[4]

    concurrenciaA = [0]
    colaA = [0]
    erroresA = [0]

    concurrenciaB = [0]
    colaB = [0]
    erroresB = [0]

    concurrenciaC = [0]
    colaC = [0]
    erroresC = [0]

    visitas = []
    visitasFinalizadas = []
    errores = []

    tiempoRespuesta = {"A": [], "B":[], "C":[]}

    llegadas = {"A": [], "B":[], "C":[]}
    arriveX = {"A": 0, "B": 0, "C":0}
    arriveY = {"A": [], "B":[], "C":[]}

    stepCount, stepsTime, steps = arrivalSteps(meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba)

    segundo = 0
    for stepIndex in range(stepCount):
        
        tiempoStep = 0
        while tiempoStep < stepsTime[stepIndex]:
            print(segundo)
            
            bloque.bloqueSimulacion(True, "A", NULL, meanVisitas1, devVisitas1, steps[stepIndex], limiteConcurrencia1, limiteCola1, visitas, llegadas)
        
            bloque.bloqueSimulacion(False, "B", "A", meanVisitas2, devVisitas2, steps[stepIndex], limiteConcurrencia2, limiteCola2, visitas, llegadas)
        
            bloque.bloqueSimulacion(False, "C", "B", meanVisitas3, devVisitas3, steps[stepIndex], limiteConcurrencia3, limiteCola3, visitas, llegadas)
            
            
            checkFinish(visitas, errores, erroresA, erroresB, erroresC, concurrenciaA, concurrenciaB, concurrenciaC, colaA, colaB, colaC, visitasFinalizadas, tiempoRespuesta)

            

            tiempoStep = tiempoStep + 1
            segundo = segundo + 1
            concurrenciaA.append(0)
            concurrenciaB.append(0)
            concurrenciaC.append(0)
            colaA.append(0)
            colaB.append(0)
            colaC.append(0)
            erroresA.append(0)
            erroresB.append(0)
            erroresC.append(0)

    ##print(visitas, visitasFinalizadas)

    while len(visitas) > 0:
        print(segundo)

        bloque.bloqueSimulacion(True, "A", NULL, meanVisitas1, devVisitas1, 0, limiteConcurrencia1, limiteCola1, visitas, llegadas)
        
        bloque.bloqueSimulacion(False, "B", "A", meanVisitas2, devVisitas2, steps[stepIndex], limiteConcurrencia2, limiteCola2, visitas, llegadas)
        
        bloque.bloqueSimulacion(False, "C", "B", meanVisitas3, devVisitas3, steps[stepIndex], limiteConcurrencia3, limiteCola3, visitas, llegadas)
        
        checkFinish(visitas, errores, erroresA, erroresB, erroresC, concurrenciaA, concurrenciaB, concurrenciaC, colaA, colaB, colaC, visitasFinalizadas, tiempoRespuesta)


        segundo = segundo + 1
        if len(visitas) > 0:
            concurrenciaA.append(0)
            concurrenciaB.append(0)
            concurrenciaC.append(0)
            colaA.append(0)
            colaB.append(0)
            colaC.append(0)
            erroresA.append(0)
            erroresB.append(0)
            erroresC.append(0)
    #print(visitas, visitasFinalizadas)
    
    concurrencias = [concurrenciaA, concurrenciaB, concurrenciaC]
    colas = [colaA, colaB, colaC]
    errores = [erroresA, erroresB, erroresC]
    poissonDataArrange(llegadas, arriveX, arriveY)
    plotSetUp(duracionPrueba, segundo, visitasFinalizadas, ["A", "B", "C"], tiempoRespuesta, concurrencias, colas, errores, llegadas, arriveX, arriveY)
    


        

def rendimiento(tiempo, llegadas, finalizadas, rendStep):
    tiempoNuevo = []
    llegadasNuevo = []
    finalizadasNuevo = []
    for segundo in tiempo:
        if segundo == 0:
            tiempoNuevo.append(segundo)
            llegadasNuevo.append(llegadas[segundo])
            finalizadasNuevo.append(len(finalizadas[segundo]))
        else:

            step = int(rendStep)*60
            if (segundo) % step == 0:
                tiempoNuevo.append(segundo)
                if segundo >= len(llegadas):
                    llegadasNuevo.append(0)
                else:
                    llegadasNuevo.append(llegadas[segundo])
                finalizadasNuevo.append(len(finalizadas[segundo]))
            else:
                if segundo >= len(llegadas):
                    llegadasNuevo[-1] = llegadasNuevo[-1] + 0
                else:
                    llegadasNuevo[-1] = llegadasNuevo[-1] + llegadas[segundo] 
                finalizadasNuevo[-1] = finalizadasNuevo[-1] + len(finalizadas[segundo])
    
    return tiempoNuevo, llegadasNuevo, finalizadasNuevo