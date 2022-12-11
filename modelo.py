from posturas import *
import scipy.optimize as sp
import matplotlib.pyplot as plt

def EjecutarModelo(app, posturas, listRestricciones, fo):
    placer_posturas = [int(x.placer) for x in posturas]
    agotamiento_posturas = [int(x.agotamiento) for x in posturas]
    restricciones = CrearRestricciones(listRestricciones, placer_posturas, agotamiento_posturas)
    resultado = Modelo(app.minimizar.get(), app.energia_ini.get(), app.umbral_org.get(), restricciones, fo, app.placer_ini.get(), len(placer_posturas))

    return resultado

def CrearRestricciones(listRestricciones, placer_posturas, agotamiento_posturas):
    restr = []
    for i in listRestricciones:
        if i == 'TodosVivos':
            restr.append((agotamiento_posturas, 0))
        elif i == 'TodosOrgasmo':
            restr.append((placer_posturas, 1))
    return restr

def Modelo(minimizar, ei, uo, restr, crit, pi, cant_post):
    list = []
    for i in restr:
        if i[1] == 1:
            list.append( [(-1 * item) for item in i[0]])
            uo = -1 * uo
        else:
            list.append(i[0])

    a_ub_1 = list
    
    fo = []
    if(minimizar == True):
        fo = [int(item) for item in crit]
    else:
        fo = [(-1 *int(item)) for item in crit]

    b_ub = [ei, pi + uo]
    
    boundss = []
    for i in range(cant_post):
        boundss.append((0, None))

    return sp.linprog(c=fo, A_ub = a_ub_1, b_ub = b_ub , bounds=boundss)