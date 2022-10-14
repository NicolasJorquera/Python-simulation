
from numpy import pad, random
import numpy as np 
import bloque
import bloques
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

def checkFinish(visitas,concurrenciaA, concurrenciaB, concurrenciaC, concurrenciaD, colaA, colaB, colaC, colaD, erroresA, erroresB, erroresC, erroresD, filtradosA, filtradosB, filtradosC, filtradosD, visitasFinalizadas, tiempoRespuesta):
    offset = 0
    tiempoRespuestaSuma = {"A":[], "B":[], "C":[], "D":[]}
    for visitaIndex in range(len(visitas)):
        visitaIndex = visitaIndex - offset
        if visitas[visitaIndex].get("estado A") != None:
            if visitas[visitaIndex]["estado A"] == "Error":
                erroresA[-1] = erroresA[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado A"] == "Filtrado":
                filtradosA[-1] = filtradosA[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado A"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado A"] == "Concurrencia":
                concurrenciaA[-1] = concurrenciaA[-1] + 1
            elif visitas[visitaIndex]["estado A"] == "Cola":
                colaA[-1] = colaA[-1] + 1

        if visitas[visitaIndex].get("estado B") != None:
            if visitas[visitaIndex]["estado B"] == "Error":
                erroresA[-1] = erroresA[-1] + 1
                erroresB[-1] = erroresB[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado B"] == "Filtrado":
                filtradosB[-1] = filtradosB[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado B"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado B"] == "Concurrencia":
                concurrenciaB[-1] = concurrenciaB[-1] + 1
            elif visitas[visitaIndex]["estado B"] == "Cola":
                colaB[-1] = colaB[-1] + 1
        
        if visitas[visitaIndex].get("estado C") != None:
            if visitas[visitaIndex]["estado C"] == "Error":
                erroresA[-1] = erroresA[-1] + 1
                erroresB[-1] = erroresB[-1] + 1
                erroresC[-1] = erroresC[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado C"] == "Filtrado":
                filtradosC[-1] = filtradosC[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado C"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado C"] == "Concurrencia":
                concurrenciaC[-1] = concurrenciaC[-1] + 1
            elif visitas[visitaIndex]["estado C"] == "Cola":
                colaC[-1] = colaC[-1] + 1

            if visitas[visitaIndex]["estado C"] == "Concurrencia, bloque finalizado":
                tiempoRespuestaSuma["A"].append(visitas[visitaIndex]["tiempoRespuesta A"])
                tiempoRespuestaSuma["B"].append(visitas[visitaIndex]["tiempoRespuesta B"])
                tiempoRespuestaSuma["C"].append(visitas[visitaIndex]["tiempoRespuesta C"])

                visitasFinalizadas.append(visitas[visitaIndex])
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
        if visitas[visitaIndex].get("estado D") != None:
            if visitas[visitaIndex]["estado D"] == "Error":
                erroresA[-1] = erroresA[-1] + 1
                erroresB[-1] = erroresB[-1] + 1
                erroresD[-1] = erroresD[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado D"] == "Filtrado":
                filtradosD[-1] = filtradosD[-1] + 1
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
            elif visitas[visitaIndex]["estado D"] == "Concurrencia, bloque finalizado" or  visitas[visitaIndex]["estado D"] == "Concurrencia":
                concurrenciaD[-1] = concurrenciaD[-1] + 1
            elif visitas[visitaIndex]["estado D"] == "Cola":
                colaD[-1] = colaD[-1] + 1

            if visitas[visitaIndex]["estado D"] == "Concurrencia, bloque finalizado":
                tiempoRespuestaSuma["A"].append(visitas[visitaIndex]["tiempoRespuesta A"])
                tiempoRespuestaSuma["B"].append(visitas[visitaIndex]["tiempoRespuesta B"])
                tiempoRespuestaSuma["D"].append(visitas[visitaIndex]["tiempoRespuesta D"])

                visitasFinalizadas.append(visitas[visitaIndex])
                visitas.pop(visitaIndex)
                offset = offset + 1
                continue
    if len(tiempoRespuestaSuma["A"]) > 0 or len(tiempoRespuestaSuma["B"]) > 0 or len(tiempoRespuestaSuma["C"]) > 0 or len(tiempoRespuestaSuma["D"]) > 0:
        if len(tiempoRespuestaSuma["A"]) > 0:
            tiempoRespuesta["A"].append(np.mean(tiempoRespuestaSuma["A"]))
        # elif len(tiempoRespuesta["A"]) > 0:
        #     tiempoRespuesta["A"].append(tiempoRespuesta["A"][-1])
        if len(tiempoRespuestaSuma["B"]) > 0:
            tiempoRespuesta["B"].append(np.mean(tiempoRespuestaSuma["B"]))
        # elif len(tiempoRespuesta["B"]) > 0:
        #     tiempoRespuesta["B"].append(tiempoRespuesta["B"][-1])
        if len(tiempoRespuestaSuma["C"]) > 0:
            tiempoRespuesta["C"].append(np.mean(tiempoRespuestaSuma["C"]))
        # elif len(tiempoRespuesta["C"]) > 0:
        #     tiempoRespuesta["C"].append(tiempoRespuesta["C"][-1])
        if len(tiempoRespuestaSuma["D"]) > 0:
            tiempoRespuesta["D"].append(np.mean(tiempoRespuestaSuma["D"]))
        # elif len(tiempoRespuesta["D"]) > 0:
        #     tiempoRespuesta["D"].append(tiempoRespuesta["D"][-1])

def plotSetUp(duracionPrueba, tiempoTotal, finalizadas, bloques, tiempoRespuesta, concurrencias, colas, errores, filtrados, llegadas, arriveX, arriveY, rendSteps):
    
    for letraBloqueIndex in range(len(bloques)):
        plot.plot(duracionPrueba, tiempoTotal,finalizadas[bloques[letraBloqueIndex]], bloques[letraBloqueIndex], tiempoRespuesta[bloques[letraBloqueIndex]], concurrencias[letraBloqueIndex], 
        colas[letraBloqueIndex], errores[letraBloqueIndex], filtrados[letraBloqueIndex], llegadas[bloques[letraBloqueIndex]], range(arriveX[bloques[letraBloqueIndex]]  + 1), arriveY[bloques[letraBloqueIndex]], rendSteps[letraBloqueIndex] )
        
    
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
    meanVisitas1, devVisitas1, meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba, limiteConcurrencia1, limiteCola1, rendStep1 = info[0]
    dist1 = int(info[1])
    meanVisitas2, devVisitas2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia2, limiteCola2, rendStep2 = info[2]
    dist2 = int(info[3])
    meanVisitas3, devVisitas3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia3, limiteCola3, rendStep3 = info[4]
    dist3 = int(info[5])
    meanVisitas4, devVisitas4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, limiteConcurrencia4, limiteCola4, rendStep4 = info[6]

    concurrenciaA = [0]
    colaA = [0]
    erroresA = [0]
    filtradosA = [0]

    concurrenciaB = [0]
    colaB = [0]
    erroresB = [0]
    filtradosB = [0]

    concurrenciaC = [0]
    colaC = [0]
    erroresC = [0]
    filtradosC = [0]

    concurrenciaD = [0]
    colaD = [0]
    erroresD = [0]
    filtradosD = [0]

    visitas = []
    visitasFinalizadas = []
    errores = []
    filtrados = []

    tiempoRespuesta = {"A": [], "B":[], "C":[], "D":[]}

    llegadas = {"A": [], "B":[], "C":[], "D":[]}
    arriveX = {"A": 0, "B": 0, "C":0, "D":0}
    arriveY = {"A": [], "B":[], "C":[], "D":[]}
    finalizadas = {"A": [], "B":[], "C":[], "D":[]}

    stepCount, stepsTime, steps = arrivalSteps(meanLlegadas1, meanLlegadas2, meanLlegadas3, meanLlegadas4, meanLlegadas5, meanLlegadas6, meanLlegadas7, duracionPrueba)

    segundo = 0
    for stepIndex in range(stepCount):
        
        tiempoStep = 0
        while tiempoStep < stepsTime[stepIndex]:
            print(segundo)
            
            bloque.bloqueSimulacion(True, "A", NULL, meanVisitas1, devVisitas1, steps[stepIndex], limiteConcurrencia1, limiteCola1, visitas, llegadas, finalizadas, NULL)

            bloque.bloqueSimulacion(False, "B", "A", meanVisitas2, devVisitas2, steps[stepIndex], limiteConcurrencia2, limiteCola2, visitas, llegadas, finalizadas, dist1)

            CInfo = meanVisitas3, devVisitas3, steps[stepIndex], limiteConcurrencia3, limiteCola3, visitas, llegadas, finalizadas, dist2
            DInfo = meanVisitas4, devVisitas4, steps[stepIndex], limiteConcurrencia4, limiteCola4, visitas, llegadas, finalizadas, dist3
            bloques.bloquesSimulacion("C", "D", "B", CInfo, DInfo)
            

            
            checkFinish(visitas, concurrenciaA, concurrenciaB, concurrenciaC, concurrenciaD, colaA, colaB, colaC, colaD, 
        erroresA, erroresB, erroresC, erroresD, filtradosA, filtradosB, filtradosC, filtradosD, visitasFinalizadas, tiempoRespuesta)

            

            tiempoStep = tiempoStep + 1
            segundo = segundo + 1
            concurrenciaA.append(0)
            concurrenciaB.append(0)
            concurrenciaC.append(0)
            concurrenciaD.append(0)
            colaA.append(0)
            colaB.append(0)
            colaC.append(0)
            colaD.append(0)
            erroresA.append(0)
            erroresB.append(0)
            erroresC.append(0)
            erroresD.append(0)
            filtradosA.append(0)
            filtradosB.append(0)
            filtradosC.append(0)
            filtradosD.append(0)

    ##print(visitas, visitasFinalizadas)

    while len(visitas) > 0:
        print(segundo)

        bloque.bloqueSimulacion(True, "A", NULL, meanVisitas1, devVisitas1, 0, limiteConcurrencia1, limiteCola1, visitas, llegadas, finalizadas, NULL)
        
        bloque.bloqueSimulacion(False, "B", "A", meanVisitas2, devVisitas2, steps[stepIndex], limiteConcurrencia2, limiteCola2, visitas, llegadas, finalizadas, dist1)
        
        CInfo = meanVisitas3, devVisitas3, steps[stepIndex], limiteConcurrencia3, limiteCola3, visitas, llegadas, finalizadas, dist2
        DInfo = meanVisitas4, devVisitas4, steps[stepIndex], limiteConcurrencia4, limiteCola4, visitas, llegadas, finalizadas, dist3
        bloques.bloquesSimulacion("C", "D", "B", CInfo, DInfo)

        checkFinish(visitas, concurrenciaA, concurrenciaB, concurrenciaC, concurrenciaD, colaA, colaB, colaC, colaD, 
        erroresA, erroresB, erroresC, erroresD, filtradosA, filtradosB, filtradosC, filtradosD, visitasFinalizadas, tiempoRespuesta)


        segundo = segundo + 1
        if len(visitas) > 0:
            concurrenciaA.append(0)
            concurrenciaB.append(0)
            concurrenciaC.append(0)
            concurrenciaD.append(0)
            colaA.append(0)
            colaB.append(0)
            colaC.append(0)
            colaD.append(0)
            erroresA.append(0)
            erroresB.append(0)
            erroresC.append(0)
            erroresD.append(0)
            filtradosA.append(0)
            filtradosB.append(0)
            filtradosC.append(0)
            filtradosD.append(0)

    
    concurrencias = [concurrenciaA, concurrenciaB, concurrenciaC, concurrenciaD]
    colas = [colaA, colaB, colaC, colaD]
    errores = [erroresA, erroresB, erroresC, erroresD]
    filtrados = [filtradosA, filtradosB, filtradosC, filtradosD]
    rendSteps = [rendStep1, rendStep2, rendStep3, rendStep4]
    poissonDataArrange(llegadas, arriveX, arriveY)
    plotSetUp(duracionPrueba, segundo, finalizadas, ["A", "B", "C", "D"], tiempoRespuesta, concurrencias, colas, errores, filtrados, llegadas, arriveX, arriveY, rendSteps)
    


        

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

            step = int(rendStep)*60
            if (segundo) % step == 0:
                tiempoNuevo.append(segundo)
                if segundo >= len(llegadas):
                    llegadasNuevo.append(0)
                else:
                    llegadasNuevo.append(llegadas[segundo])
                finalizadasNuevo.append(finalizadas[segundo])
            else:
                if segundo >= len(llegadas):
                    llegadasNuevo[-1] = llegadasNuevo[-1] + 0
                else:
                    llegadasNuevo[-1] = llegadasNuevo[-1] + llegadas[segundo] 
                finalizadasNuevo[-1] = finalizadasNuevo[-1] + finalizadas[segundo]
    for index in range(len(llegadasNuevo)):
        llegadasNuevo[index] = llegadasNuevo[index]/(int(rendStep)*60)
        finalizadasNuevo[index] = finalizadasNuevo[index]/(int(rendStep)*60)
     
    
    return tiempoNuevo, llegadasNuevo, finalizadasNuevo
