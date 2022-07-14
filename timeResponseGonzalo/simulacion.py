
from numpy import pad, random
import numpy as np 
import bloque

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

def simulacion(info):
    meanVisitas1, devVisitas1, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba, limiteConcurrencia1, limiteCola1 = info[0]
    dist1 = int(info[1])
    meanVisitas2, devVisitas2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia2, limiteCola2 = info[2]
    dist2 = int(info[3])
    meanVisitas3, devVisitas3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia3, limiteCola3 = info[4]

    concurrencia1 = []
    cola1 = []

    concurrencia2 = []
    cola2 = []

    concurrencia3 = []
    cola3 = []

    visitas = []
    visitasFinalizadas = []

    stepCount, stepsTime, steps = arrivalSteps(meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba)

    segundo = 0
    for stepIndex in range(stepCount):
        
        tiempoStep = 0
        while tiempoStep < stepsTime[stepIndex]:
            print(segundo)

            
            visitas = bloque.bloqueSimulacion(True, "A", NULL, meanVisitas1, devVisitas1, steps[stepIndex], limiteConcurrencia1, limiteCola1, visitas)
        
            visitas = bloque.bloqueSimulacion(False, "B", "A", meanVisitas2, devVisitas2, steps[stepIndex], limiteConcurrencia2, limiteCola2, visitas)
            
            visitas = bloque.bloqueSimulacion(False, "C", "B", meanVisitas3, devVisitas3, steps[stepIndex], limiteConcurrencia3, limiteCola3, visitas)
            
            offset = 0
            for visitaIndex in range(len(visitas)):
                visitaIndex = visitaIndex - offset
                if visitas[visitaIndex].get("estado A") != None:
                    if visitas[visitaIndex]["estado A"] == "Al agua":
                        visitasFinalizadas.append(visitas[visitaIndex])
                        visitas.pop(visitaIndex)
                        offset = offset + 1
                        continue

                if visitas[visitaIndex].get("estado B") != None:
                    if visitas[visitaIndex]["estado B"] == "Al agua":
                        visitasFinalizadas.append(visitas[visitaIndex])
                        visitas.pop(visitaIndex)
                        offset = offset + 1
                        continue
                
                if visitas[visitaIndex].get("estado C") != None:
                    if visitas[visitaIndex]["estado C"] == "Concurrencia, bloque finalizado" or visitas[visitaIndex]["estado C"] == "Al agua":
                        visitasFinalizadas.append(visitas[visitaIndex])
                        visitas.pop(visitaIndex)
                        offset = offset + 1
                        continue

            
            tiempoStep = tiempoStep + 1
            segundo = segundo + 1

    print(visitas, visitasFinalizadas)
    


        

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
            if segundo >= len(llegadas):
                llegadas.append(0)

            step = int(rendStep)*60
            if (segundo) % step == 0:
                tiempoNuevo.append(segundo)
                llegadasNuevo.append(llegadas[segundo])
                finalizadasNuevo.append(len(finalizadas[segundo]))
            else:
                llegadasNuevo[-1] = llegadasNuevo[-1] + llegadas[segundo] 
                finalizadasNuevo[-1] = finalizadasNuevo[-1] + len(finalizadas[segundo])
    
    return tiempoNuevo, llegadasNuevo, finalizadasNuevo