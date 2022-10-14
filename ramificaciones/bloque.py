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
    

def bloqueSimulacion(isBase, letraBloque, letraBloqueAnterior, meanVisitas, devVisitas, meanLlegadas, limiteConcurrencia, limiteCola, visitasGlobales, llegadas, finalizadas, dist):

    concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque)
    concurrencia, cola, visitasGlobales = ColaToConcurrencia(concurrencia, cola, limiteConcurrencia, visitasGlobales, letraBloque)
    
    mu = int(meanVisitas)
    dev = int(devVisitas)



    if isBase:
      
        
        if meanLlegadas == 0:
            visitas = 0
        else:
            visitas = random.poisson(lam=int(meanLlegadas), size=1)
            visitas = visitas[0]
            llegadas[letraBloque].append(visitas)
        for visita in range(visitas):
            tiempoVisita = np.random.normal(mu, dev, 1)
            tiempoVisita = round(tiempoVisita[0])
            while tiempoVisita < 0:
                tiempoVisita = np.random.normal(mu, dev, 1)
                tiempoVisita = round(tiempoVisita[0])

            
                
            visita={}
            visita["estado "+ letraBloque] = "Creado en " + letraBloque
            visita["tiempoVisita " +letraBloque] = tiempoVisita 
            visita["tiempoVisitaRestante " +letraBloque] = tiempoVisita
            visita["tiempoEjecucion " +letraBloque] = -1
            visita["tiempoCola " +letraBloque] = 0
            visita["tiempoRespuesta " +letraBloque] = -1

            concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque)

            if concurrencia < int(limiteConcurrencia):
                visita["estado " + letraBloque] = "Concurrencia"
                visitasGlobales.append(visita)
            else:
                if cola < int(limiteCola):
                    visita["estado " +letraBloque] = "Cola"
                    visitasGlobales.append(visita)
                else:
                    visita["estado " +letraBloque] = "Error"
                    visitasGlobales.append(visita)
    else:
        #escribir si las llegadas vienen de otro bloque
        visitas = 0
        
        for visita in visitasGlobales:
            
            if visita.get("estado "+letraBloqueAnterior) != None:
                rd = random.random()
                if visita["estado "+ letraBloqueAnterior] == "Concurrencia, bloque finalizado":
                    if rd > dist/100:
                        if visita.get("estado "+letraBloque) == None:
                            visita["estado "+ letraBloque] = "Filtrado"
                            visita["tiempoVisitaRestante " + letraBloque] = -1
                            visita["tiempoEjecucion " + letraBloque] = 0
                            visita["tiempoCola " + letraBloque] = 0
                            visita["tiempoRespuesta " + letraBloque] = 0
                    else:
                        if visita.get("estado "+letraBloque) == None:
                            visitas = visitas + 1
                            visita["estado "+ letraBloque] = "Creado en " + letraBloque

                            tiempoVisita = np.random.normal(mu, dev, 1)
                            tiempoVisita = round(tiempoVisita[0])
                            while tiempoVisita < 0:
                                tiempoVisita = np.random.normal(mu, dev, 1)
                                tiempoVisita = round(tiempoVisita[0])
                            visita["tiempoVisita " + letraBloque] = tiempoVisita 
                            visita["tiempoVisitaRestante " + letraBloque] = tiempoVisita
                            visita["tiempoEjecucion " + letraBloque] = -1
                            visita["tiempoCola " + letraBloque] = 0
                            visita["tiempoRespuesta " + letraBloque] = -1

                            concurrencia, cola = findConcurrenciaCola(visitasGlobales, letraBloque)
                        
                            if concurrencia < int(limiteConcurrencia):
                                visita["estado " + letraBloque] = "Concurrencia"
                            else:
                                if cola < int(limiteCola):
                                    visita["estado " +letraBloque] = "Cola"
                                else:
                                    visita["estado " +letraBloque] = "Error"
        
        llegadas[letraBloque].append(visitas)
        
    


    finalizadasBloque = 0
    for visita in visitasGlobales:
        if visita.get("estado "+letraBloque) != None and visita.get("estado "+letraBloque) != "Error" and visita.get("estado "+letraBloque) != "Filtrado":
            if visita["tiempoVisitaRestante " + letraBloque] <= 0 and visita["estado "+ letraBloque] != "Concurrencia, bloque finalizado":
                
                visita["estado "+ letraBloque] = "Concurrencia, bloque finalizado"
                finalizadasBloque = finalizadasBloque + 1


            ##solo para los de concurrencia
            if visita["estado "+ letraBloque] == "Concurrencia, bloque finalizado" or visita["estado "+letraBloque] == "Concurrencia":
                visita["tiempoVisitaRestante " + letraBloque] = visita["tiempoVisitaRestante " + letraBloque] - 1
                visita["tiempoEjecucion " + letraBloque] = visita["tiempoEjecucion " + letraBloque] + 1

            if visita["estado "+letraBloque] == "Cola":
                visita["tiempoCola " + letraBloque] = visita["tiempoCola " + letraBloque] + 1
            
            
            visita["tiempoRespuesta "+ letraBloque] = visita["tiempoRespuesta " + letraBloque] + 1
    
    finalizadas[letraBloque].append(finalizadasBloque)



    
