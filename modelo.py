from posturas import *
from restricciones import *
import scipy.optimize as sp
import matplotlib.pyplot as plt

def EjecutarModelo(minimizar, criterio, umbral_org, energia_ini, placer_ini, listRestricciones, fo):
    placer_posturas = [x.placer for x in posturas]
    agotamiento_posturas = [x.agotamiento for x in posturas]
    restricciones = CrearRestricciones(listRestricciones, placer_posturas, agotamiento_posturas)
    resultado = Modelo(minimizar, energia_ini, umbral_org, restricciones, fo, placer_ini)

    return resultado

def CrearRestricciones(listRestricciones, placer_posturas, agotamiento_posturas):
    restr = []
    for i in listRestricciones:
        if i == 'a':
            restr.append((agotamiento_posturas, 0))
        elif i == 'b':
            restr.append((placer_posturas, 1))
    return restr

def Modelo(minimizar, ei, uo, restr, crit, pi):
    list = []
    for i in restr:
        if i[1] == 1:
            list.append( [(-1 * item) for item in i[0]])
            uo = -1 * uo
        else:
            list.append(i[0])

    a_ub_1 = list
    #a_ub_1.append([0, -1, 0])
    #a_ub_1.append([-1, 0, 0])
    #a_ub_1.append([0, 0, -1])

    fo = []
    if(minimizar == True):
        fo = [int(item) for item in crit]
    else:
        fo = [(-1 *int(item)) for item in crit]

    b_ub = [ei, pi + uo]
    
    bounds1 = (1, None)
    bounds2 = (1, None)
    bounds3 = (1, None)
    bounds4 = (1, None)
    bounds5 = (1, None)
    

    return sp.linprog(c=fo, A_ub = a_ub_1, b_ub = b_ub , bounds=[bounds1, bounds2, bounds3, bounds4, bounds5])