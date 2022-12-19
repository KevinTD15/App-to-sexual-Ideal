from posturas import *
import scipy.optimize as sp

def EjecutarModelo(app, listPersonasPosturas, listRestricciones, fo):
    restricciones = CrearRestricciones(listRestricciones, listPersonasPosturas)
    resultado = Modelo(app.minimizar.get(), restricciones, fo, len(listPersonasPosturas[0].posturas))

    return resultado

def CrearRestricciones(listRestricciones, listPersonasPosturas):
    restr = []
    for i in listRestricciones:
        for p in listPersonasPosturas: 
            restr1 = []
            restr2 = []
            for j in p.posturas:   
                if i == 'TodosVivos':
                    restr1.append(int(j.agotamiento))
                    if(j == p.posturas[len(p.posturas) - 1]):
                        restr.append((restr1, int(p.energiaInicial), 0))
                elif i == 'TodosOrgasmo':
                    restr2.append(int(j.placer))
                    if(j == p.posturas[len(p.posturas) - 1]):
                        restr.append((restr2, int(p.placerInicial), int(p.umbralOrgasmo), 1))
    return restr

def Modelo(minimizar, restr, crit, cant_post):
    a_ub_1 = []
    b_ub = []
    
    for i in restr:
        if i[len(i) - 1] == 0:
            a_ub_1.append(i[0])
            b_ub.append(i[1])
        else:
            a_ub_1.append( [(-1 * item) for item in i[0]])
            b_ub.append(i[1] - i[2])
            

    
    fo = []
    if(minimizar == True):
        fo = [int(item) for item in crit]
    else:
        fo = [(-1 *int(item)) for item in crit]

    boundss = []
    for i in range(cant_post):
        boundss.append((0, None))

    return sp.linprog(c=fo, A_ub = a_ub_1, b_ub = b_ub , bounds=boundss)