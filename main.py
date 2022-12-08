import numpy as np
import numpy as np
from posturas import *
from modelo import *

minimizar = False
criterio = None
umbral_org = 0
energia_ini = 0

# def read_script(minimizar, umbral_org, energia_ini): #poner criterio
#     with open ('script.txt') as f :
#         lines = f.readlines()
#     if(lines[0] == 'minimizar\n'):
#         minimizar = True
#     fo = lines[1].split(' ')
#     list_placer = lines[2].split(' ')
#     for i in range(len(list_placer)):
#         posturas[i].placer = list_placer[i]
#     list_agot = lines[3].split(' ')
#     for i in range(len(list_agot)):
#         posturas[i].agotamiento = list_agot[i]
                    
#     energia_ini = int(lines[4])
#     umbral_org = int(lines[5])
#     list_restr = lines[6].split(' ')
#     criterio = lines[7]
#     return minimizar, energia_ini, umbral_org, list_restr, criterio, fo

# var_decision = {}
# var_decision.update(tiempo_posicion = 't')
# var_decision.update(cuan_duro = 'cd')

def main():
    fin = ''
    while fin != '1':
        #minimizar = False
        #criterio = None
        #umbral_org = 0
        #energia_ini = 0
        print('''Las posturas son:
              1- Misionero
              2- Perrito
              3- 69
              ''')
        print('''Desea:
              1- Maximizar
              2- Minimizar''')
        minimizar = input() == '2'
        print('''Criterio:
              1- Tiempo''')
        criterio = input()   
        print('Teclee el umbral de orgasmo')
        umbral_org = int(input())  
        print('Teclee la energia inicial')
        energia_ini = int(input())
        print('Teclee el placer inicial')
        placer_ini = int(input())
        print(f'Tecle los {len(posturas)} valores de la funcion objetivo')
        fo = [int(x) for x in input().split(' ')]
        for i in posturas:
            print(f'Teclee cuanto placer da la postura {i.nombre}')
            i.placer = int(input()) 
        for i in posturas:
            print(f'Teclee cuanto cansa da la postura {i.nombre}')
            i.agotamiento = int(input()) 
        print('''Restricciones que desea usar (insertar en la consola por espacios):
              a- TodosVivos
              b- TodosOrgasmo''')  
        listRestricciones = input().split(' ')
        resultado = EjecutarModelo(minimizar, criterio, umbral_org, energia_ini, placer_ini, listRestricciones, fo)
        
        for i in range(len(resultado.x)):
            print(f'El tiempo que hay que dedicarle a la postura {posturas[i].nombre} es {resultado.x[i]}')
        fig, ax = plt.subplots()
        p = [x.nombre for x in posturas]
        plt.bar(p, resultado.x)
        ax.legend(loc = 'best')
        plt.show()
# def main():
#     s = read_script(minimizar, umbral_org, energia_ini)
#     restr = crearRestricciones(s[3])
#     a = modelo(s[0], s[1], s[2], restr, s[5])

#     tiempo = a.x
#     placer = [int(item.placer) for item in posturas]
#     cansancio = [int(item.agotamiento) for item in posturas]

#     fig, ax = plt.subplots()
#     temperaturas = {'Placer':placer, 'Cansancio':cansancio}
#     ax.plot(tiempo, placer, label = 'Placer')
#     ax.plot(tiempo, cansancio, label = 'Cansancio')
#     ax.legend(loc = 'best')
#     plt.show()

#     for i in range(len(a.x)):
#         print(f'El {s[4]} que hay que dedicarle a la postura {posturas[i].name} es {a.x[i]}')

if __name__ == '__main__':
    main()