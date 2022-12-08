from posturas import *
from restricciones import *
import scipy.optimize as sp

def EjecutarModelo(minimizar, criterio, umbral_org, energia_ini, placer_ini, listRestricciones):
    placer_posturas = [x.placer for x in posturas]
    agotamiento_posturas = [x.agotamiento for x in posturas]
    restricciones = CrearRestricciones(listRestricciones, placer_posturas, agotamiento_posturas)
    resultado = Modelo(minimizar, energia_ini, umbral_org, restricciones, criterio)
    
    return resultado

def CrearRestricciones(listRestricciones, placer_posturas, agotamiento_posturas):
    restr = []
    for i in listRestricciones:
        if i == 'a':
            restr.append((agotamiento_posturas, 0))
        elif i == 'b':
            restr.append((placer_posturas, 1))
    return restr

def Modelo(minimizar, ei, uo, restr, crit):
    list = []
    for i in restr:
        if i[1] == 1:
            list.append( [(-1 * item) for item in i[0]])
        else:
            list.append(i[0])

    a_ub_1 = list

    fo = []
    if(minimizar == True):
        fo = [int(item) for item in crit]
    else:
        fo = [(-1 *int(item)) for item in crit]

    b_ub = [ei, uo]
    

    return sp.linprog(c=fo, A_ub = a_ub_1, b_ub = b_ub ,bounds=(0, None))