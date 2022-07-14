import numpy as np 
from numpy import pad, random

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
    

def bloqueSimulacion(isBase, letraBloque, letraBloqueAnterior, meanVisitas, devVisitas, meanLlegadas, limiteConcurrencia, limiteCola, visitasGlobales):

    concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque)
    concurrencia, cola, visitasGlobales = ColaToConcurrencia(concurrencia, cola, limiteConcurrencia, visitasGlobales, letraBloque)
    
    mu = int(meanVisitas)
    dev = int(devVisitas)
        

    if isBase:
      
        

        visitas = random.poisson(lam=int(meanLlegadas), size=1)
        visitas = visitas[0]
        for visita in range(visitas):
            tiempoVisita = np.random.normal(mu, dev, 1)
            tiempoVisita = truncate(tiempoVisita[0])
            visita = {
                "estado "+letraBloque: "Creado en A",
                "tiempoVisitaRestante " +letraBloque: tiempoVisita,
                "tiempoRespuesta " +letraBloque: 0 #Esto incluye los tiempos de espera
            }

            concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque)

            if concurrencia < int(limiteConcurrencia):
                visita["estado " + letraBloque] = "Concurrencia"
                visitasGlobales.append(visita)
            else:
                if cola < int(limiteCola):
                    visita["estado " +letraBloque] = "Cola"
                    visitasGlobales.append(visita)
                else:
                    visita["estado " +letraBloque] = "Al agua"
                    visitasGlobales.append(visita)
    else:
        #escribir si las llegadas vienen de otro bloque
        for visita in visitasGlobales:
            if visita.get("estado "+letraBloqueAnterior) != None:
                if visita["estado "+ letraBloqueAnterior] == "Concurrencia, bloque finalizado":
                    if visita.get("estado "+letraBloque) == None:
                        visita["estado "+ letraBloque] = "Creado en " + letraBloque

                        tiempoVisita = np.random.normal(mu, dev, 1)
                        tiempoVisita = truncate(tiempoVisita[0])
                        visita["tiempoVisitaRestante " +letraBloque] = tiempoVisita

                        visita["tiempoRespuesta " +letraBloque] = 0

                    concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque)
                    
                    if concurrencia < int(limiteConcurrencia):
                        visita["estado " + letraBloque] = "Concurrencia"
                    else:
                        if cola < int(limiteCola):
                            visita["estado " +letraBloque] = "Cola"
                        else:
                            visita["estado " +letraBloque] = "Al agua"
        
    



    for visita in visitasGlobales:
        if visita.get("estado "+letraBloque) != None:
            if visita["tiempoVisitaRestante " + letraBloque] <= 0:
                visita["estado "+ letraBloque] = "Concurrencia, bloque finalizado"

        
        



            visita["tiempoVisitaRestante " + letraBloque] = visita["tiempoVisitaRestante " + letraBloque] - 1
            visita["tiempoRespuesta "+ letraBloque] = visita["tiempoRespuesta " + letraBloque] + 1

    return visitasGlobales

    
