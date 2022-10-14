import numpy as np 
from numpy import pad, random
import random

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def findConcurrenciaCola(visitasGlobales, letraBloque):
    concurrencia = 0
    cola = 0
    for visita in visitasGlobales:
        if visita.get("estado "+letraBloque) != None:

            if visita["estado "+letraBloque] == "Concurrencia, bloque finalizado" or visita["estado "+letraBloque] == "Concurrencia":
                concurrencia = concurrencia + 1
            if visita["estado "+letraBloque] == "Cola":
                cola = cola + 1
    
    return concurrencia, cola

def ColaToConcurrencia(concurrencia, cola, limiteConcurrencia, visitasGlobales, letraBloque):
    for visita in visitasGlobales:
        if visita.get("estado "+letraBloque) != None:
            if cola > 0 and concurrencia < int(limiteConcurrencia) and visita["estado "+letraBloque] == "Cola":
                visita["estado "+letraBloque] = "Concurrencia"
                concurrencia = concurrencia + 1
                cola = cola - 1
    return concurrencia, cola, visitasGlobales
    

def bloquesSimulacion(letraBloque1, letraBloque2, letraBloqueAnterior, bloque1Info, bloque2Info):

    meanVisitas1, devVisitas1, meanLlegadas1, limiteConcurrencia1, limiteCola1, visitasGlobales, llegadas, finalizadas, dist1 = bloque1Info
    meanVisitas2, devVisitas2, meanLlegadas2, limiteConcurrencia2, limiteCola2, visitasGlobales, llegadas, finalizadas, dist2 = bloque2Info

    concurrencia1, cola1 = findConcurrenciaCola(visitasGlobales, letraBloque1)
    concurrencia1, cola1, visitasGlobales = ColaToConcurrencia(concurrencia1, cola1, limiteConcurrencia1, visitasGlobales, letraBloque1)

    concurrencia2, cola2 = findConcurrenciaCola(visitasGlobales, letraBloque2)
    concurrencia2, cola2, visitasGlobales = ColaToConcurrencia(concurrencia2, cola2, limiteConcurrencia2, visitasGlobales, letraBloque2)
    
    mu1 = int(meanVisitas1)
    dev1 = int(devVisitas1)

    mu2 = int(meanVisitas2)
    dev2 = int(devVisitas2)



    
    visitas1 = 0
    visitas2 = 0
    for visita in visitasGlobales:
        if visita.get("estado "+letraBloqueAnterior) != None:
            rd1 = random.random()
            rd2 = random.random()
            rd3 = random.random()
            rd4 = random.random()
            rd5 = random.random()
            bifurcado = False
            if visita["estado "+ letraBloqueAnterior] == "Concurrencia, bloque finalizado" and not(visita.get("estado "+letraBloque1) == "No bifurcado" or visita.get("estado "+letraBloque2) == "No bifurcado"):
                if  rd4 < dist1/100 +dist2/100:
                    
                    if rd3 < 0.5:
                        if rd1 < dist1/100:
                            bifurcado = True
                            if visita.get("estado "+letraBloque1) == None:
                                visitas1 = visitas1 + 1
                                visita["estado "+ letraBloque1] = "Creado en " + letraBloque1
                                visita["estado "+ letraBloque2] = "No bifurcado"

                                tiempoVisita = random.gauss(mu1, dev1)
                                tiempoVisita = round(tiempoVisita)
                                while tiempoVisita < 0:
                                    tiempoVisita = random.gauss(mu1, dev1)
                                    tiempoVisita = round(tiempoVisita)
                                visita["tiempoVisita " +letraBloque1] = tiempoVisita 
                                visita["tiempoVisitaRestante " +letraBloque1] = tiempoVisita 
                                visita["tiempoEjecucion " +letraBloque1] = -1
                                visita["tiempoCola " +letraBloque1] = 0
                                visita["tiempoRespuesta " +letraBloque1] = -1

                                concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque1)
                            
                                if concurrencia < int(limiteConcurrencia1):
                                    visita["estado " + letraBloque1] = "Concurrencia"
                                else:
                                    if cola < int(limiteCola1):
                                        visita["estado " +letraBloque1] = "Cola"
                                    else:
                                        visita["estado " +letraBloque1] = "Error"
                        elif rd2 < dist2/100:
                            bifurcado = True
                            if visita.get("estado "+letraBloque2) == None:
                                visitas2 = visitas2 + 1
                                visita["estado "+ letraBloque2] = "Creado en " + letraBloque2
                                visita["estado "+ letraBloque1] = "No bifurcado"

                                tiempoVisita = np.random.normal(mu2, dev2, 1)
                                tiempoVisita = round(tiempoVisita[0])
                                while tiempoVisita < 0:
                                    tiempoVisita = np.random.normal(mu2, dev2, 1)
                                    tiempoVisita = round(tiempoVisita[0])
                                visita["tiempoVisita " +letraBloque2] = tiempoVisita 
                                visita["tiempoVisitaRestante " +letraBloque2] = tiempoVisita 
                                visita["tiempoEjecucion " +letraBloque2] = -1
                                visita["tiempoCola " +letraBloque2] = 0
                                visita["tiempoRespuesta " +letraBloque2] = -1

                                concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque2)
                            
                                if concurrencia < int(limiteConcurrencia2):
                                    visita["estado " + letraBloque2] = "Concurrencia"
                                else:
                                    if cola < int(limiteCola2):
                                        visita["estado " +letraBloque2] = "Cola"
                                    else:
                                        visita["estado " +letraBloque2] = "Error"
                    else:
                        if rd2 < dist2/100:
                            bifurcado = True
                            if visita.get("estado "+letraBloque2) == None:
                                visitas2 = visitas2 + 1
                                visita["estado "+ letraBloque2] = "Creado en " + letraBloque2
                                visita["estado "+ letraBloque1] = "No bifurcado"

                                tiempoVisita = np.random.normal(mu2, dev2, 1)
                                tiempoVisita = round(tiempoVisita[0])
                                while tiempoVisita < 0:
                                    tiempoVisita = np.random.normal(mu2, dev2, 1)
                                    tiempoVisita = round(tiempoVisita[0])
                                visita["tiempoVisita " +letraBloque2] = tiempoVisita 
                                visita["tiempoVisitaRestante " +letraBloque2] = tiempoVisita 
                                visita["tiempoEjecucion " +letraBloque2] = -1
                                visita["tiempoCola " +letraBloque2] = 0
                                visita["tiempoRespuesta " +letraBloque2] = -1

                                concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque2)
                            
                                if concurrencia < int(limiteConcurrencia2):
                                    visita["estado " + letraBloque2] = "Concurrencia"
                                else:
                                    if cola < int(limiteCola2):
                                        visita["estado " +letraBloque2] = "Cola"
                                    else:
                                        visita["estado " +letraBloque2] = "Error"
                        elif rd1 < dist1/100:
                            bifurcado = True
                            if visita.get("estado "+letraBloque1) == None:
                                visitas1 = visitas1 + 1
                                visita["estado "+ letraBloque1] = "Creado en " + letraBloque1
                                visita["estado "+ letraBloque2] = "No bifurcado"

                                tiempoVisita = random.gauss(mu1, dev1)
                                tiempoVisita = round(tiempoVisita)
                                while tiempoVisita < 0:
                                    tiempoVisita = random.gauss(mu1, dev1)
                                    tiempoVisita = round(tiempoVisita)
                                visita["tiempoVisita " +letraBloque1] = tiempoVisita 
                                visita["tiempoVisitaRestante " +letraBloque1] = tiempoVisita 
                                visita["tiempoEjecucion " +letraBloque1] = -1
                                visita["tiempoCola " +letraBloque1] = 0
                                visita["tiempoRespuesta " +letraBloque1] = -1

                                concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque1)
                            
                                if concurrencia < int(limiteConcurrencia1):
                                    visita["estado " + letraBloque1] = "Concurrencia"
                                else:
                                    if cola < int(limiteCola1):
                                        visita["estado " +letraBloque1] = "Cola"
                                    else:
                                        visita["estado " +letraBloque1] = "Error"
                else:
                    if bifurcado == False:
                        if rd5 < 0.5:
                            visita["estado "+ letraBloque1] = "Filtrado"
                            visita["tiempoVisitaRestante " +letraBloque1] = -1
                            visita["tiempoEjecucion " +letraBloque1] = -1
                            visita["tiempoCola " +letraBloque1] = 0
                            visita["tiempoRespuesta " +letraBloque1] = -1
                        else:
                            visita["estado "+ letraBloque2] = "Filtrado"
                            visita["tiempoVisitaRestante " +letraBloque2] = -1
                            visita["tiempoEjecucion " +letraBloque2] = -1
                            visita["tiempoCola " +letraBloque2] = 0
                            visita["tiempoRespuesta " +letraBloque2] = -1
        
    llegadas[letraBloque1].append(visitas1)
    llegadas[letraBloque2].append(visitas2)
        
    


    finalizadasBloque1 = 0
    finalizadasBloque2 = 0
    for visita in visitasGlobales:
            
        if visita.get("estado "+letraBloque1) != None and visita.get("estado "+letraBloque1) != "Error" and visita.get("estado "+letraBloque1) != "Filtrado" and visita.get("estado "+letraBloque2) == "No bifurcado":
            if visita["tiempoVisitaRestante " + letraBloque1] <= 0 and visita["estado "+ letraBloque1] != "Concurrencia, bloque finalizado":
                
                visita["estado "+ letraBloque1] = "Concurrencia, bloque finalizado"
                finalizadasBloque1 = finalizadasBloque1 + 1


            ##solo para los de concurrencia
            if visita["estado "+ letraBloque1] == "Concurrencia, bloque finalizado" or visita["estado "+letraBloque1] == "Concurrencia":
                visita["tiempoVisitaRestante " + letraBloque1] = visita["tiempoVisitaRestante " + letraBloque1] - 1
                visita["tiempoEjecucion " + letraBloque1] = visita["tiempoEjecucion " + letraBloque1] + 1

            if visita["estado "+letraBloque1] == "Cola":
                visita["tiempoCola " + letraBloque1] = visita["tiempoCola " + letraBloque1] + 1
            
            
            visita["tiempoRespuesta "+ letraBloque1] = visita["tiempoRespuesta " + letraBloque1] + 1

        if visita.get("estado "+letraBloque2) != None and visita.get("estado "+letraBloque2) != "Error" and visita.get("estado "+letraBloque2) != "Filtrado" and visita.get("estado "+letraBloque1) == "No bifurcado":
            if visita["tiempoVisitaRestante " + letraBloque2] <= 0 and visita["estado "+ letraBloque2] != "Concurrencia, bloque finalizado":
                
                visita["estado "+ letraBloque2] = "Concurrencia, bloque finalizado"
                finalizadasBloque2 = finalizadasBloque2 + 1


            ##solo para los de concurrencia
            if visita["estado "+ letraBloque2] == "Concurrencia, bloque finalizado" or visita["estado "+letraBloque2] == "Concurrencia":
                visita["tiempoVisitaRestante " + letraBloque2] = visita["tiempoVisitaRestante " + letraBloque2] - 1
                visita["tiempoEjecucion " + letraBloque2] = visita["tiempoEjecucion " + letraBloque2] + 1

            if visita["estado "+letraBloque2] == "Cola":
                visita["tiempoCola " + letraBloque2] = visita["tiempoCola " + letraBloque2] + 1
            
            
            visita["tiempoRespuesta "+ letraBloque2] = visita["tiempoRespuesta " + letraBloque2] + 1
    
    finalizadas[letraBloque1].append(finalizadasBloque1)
    finalizadas[letraBloque2].append(finalizadasBloque2)



    
