from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from posturas import Postura
from personas import Persona
from modelo import EjecutarModelo
import matplotlib.pyplot as plt 
import numpy as np
import os

class Raiz():
    def __init__(self):       
        #crear ventana principal
        self.ventana = Tk()
        self.ventana.title("App-to sexual ideal")
        self.ventana.geometry("400x420"+"+"+str(10)+"+"+str(0)) 
        self.ventana.resizable(1,1)
        self.ventana.config(bg="lightblue",relief="sunken",bd=12) 

        #Label(text="Proyecto Final de PMA  2022\n\n Kevin Talavera Díaz C-311",bg="lightblue",fg="black",font=("arial",12),border=10,justify=CENTER).place(x=220,y=450)
        Label (text="Ingrese los siguientes datos",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=20)
        Button (text='Cargar Archivo',font=("arial",9),width=15,height=1,command=self.cargarFichero).place(x=250,y=20) 
        self.canvas = None
        self.vr = None
        self.boton = None 
        self.minimizar = None
        self.umbral_org = None
        self.energia_ini = None
        self.placer_ini = None
        self.canvasPosturas = None
        self.framePosturas = None
        self.canvasDatosPersona = None
        self.frameDatosPersona = None
        self.canvasFO = None
        self.frameFO = None
        self.listPersonasPosturas = None
        self.TodosVivos = None
        self.TodosOrgasmo = None
        self.personas = None
        self.button = None
        self.vp = None
        self.nombrePini = ['misionero','perrito','69','yunque','rueda']
        self.nombreP= []
        self.datosFO =None
        self.datosEntrada()

        self.ventana.mainloop() 

    def creaTablas(self):
        if self.vp == None:
            self.vp = Toplevel(self.ventana)
            self.vp.title("Datos de las posturas") 
            self.vp.geometry("430x600"+"+"+str(420)+"+"+str(0)) 
            self.vp.resizable(1,1)
            self.vp.config(bg="lightblue", bd=12, relief="sunken")
        else:
            self.canvasPosturas.destroy()
            self.canvasDatosPersona.destroy()
            self.canvasFO.destroy()

        ctdpersonas = self.personas.get()
        altoDatosPers = ctdpersonas * 20 +40+20
        altoPosturas = 20*(len(self.nombreP)+1) * ctdpersonas + 20 + 3
        altopixel = altoPosturas + altoDatosPers + 60
        self.vp.geometry("500x"+str(altopixel)+"+"+str(420)+"+"+str(0)) 

        self.tablaCaractPers()
        self.tablaPosturaPers()
        self.tablaFO()

    def tablaFO(self):
        alto = 20 * len(self.nombreP) + 20 
        self.canvasFO= Canvas(self.ventana,width=168,height=alto-2,bg='lightblue')
        self.canvasFO.grid(pady=(230,0 ),padx=(20,0))   

        self.frameFO = Frame(self.canvasFO,bg='lightblue')
        self.canvasFO.create_window((0, 0), window=self.frameFO, anchor='nw')

        fo='Tiempo'   
        #if self.criterio.get()=='1': fo='Tiempo'     
        Label(self.frameFO,text='Posturas',font=("arial",10),fg='lightblue',bg='black', width=10,height=1 , state="disabled").grid(row=0, column=0, sticky='news')
        Label(self.frameFO,text=fo,font=("arial",10),fg='lightblue',bg='black', width=10,height=1 , state="disabled").grid(row=0, column=1, sticky='news')

        self.datosFO = [[Entry() for j in range(2)] for i in range(len(self.nombreP))]
        for i in range(0,len(self.nombreP)):
            self.datosFO[i][0] = Entry(self.frameFO,textvariable=StringVar(value=self.nombreP[i]),font=("arial",10), width=10,state="disabled",bg='lightblue',fg='black')
            self.datosFO[i][0].grid(row=i+1, column=0, sticky='news')
            self.datosFO[i][1] = Entry(self.frameFO, width=8,justify=CENTER)
            self.datosFO[i][1].grid(row=i+1, column=1, sticky='news')

    def tablaCaractPers(self):
        ctdpersonas = self.personas.get()
        alto = 20 * ctdpersonas+40

        self.canvasDatosPersona= Canvas(self.vp,width=340,height=alto-5,bg='lightblue')
        self.canvasDatosPersona.grid(pady=(20,0 ),padx=(20,0))   

        self.frameDatosPersona = Frame(self.canvasDatosPersona,bg='lightblue')
        self.canvasDatosPersona.create_window((0, 0), window=self.frameDatosPersona, anchor='nw')
        
        nombreColumnas = ["Personas","energia\ninicial","placer\ninicial","umbral\norgasmo"]
        for i in range(len(nombreColumnas)):
            Label(self.frameDatosPersona,text=nombreColumnas[i],font=("arial",10),fg='lightblue',bg='black', width=10,height=2 , state="disabled").grid(row=0, column=i, sticky='news')

        self.datosPersona = [[Entry() for j in range(4)] for i in range(self.personas.get())]

        for i in range(0,self.personas.get()):
            nopers='Persona '+str(i+1)
            self.datosPersona[i][0] = Entry(self.frameDatosPersona,textvariable=StringVar(value=nopers),font=("arial",10), width=10,state="disabled",bg='lightblue',fg='black')
            self.datosPersona[i][0].grid(row=i+1, column=0, sticky='news')

            for j in range(1,4):  
                self.datosPersona[i][j] = Entry(self.frameDatosPersona, width=8,justify=CENTER)
                self.datosPersona[i][j].grid(row=i+1, column=j, sticky='news')

    def tablaPosturaPers(self):      
        ctdpersonas = self.personas.get()
        altoPosturas = 20*(len(self.nombreP)+1) * ctdpersonas + 20 + 3

        self.canvasPosturas= Canvas(self.vp,width=300,height=altoPosturas,bg='red')
        self.canvasPosturas.grid(pady=(20,0 ),padx=(20,0))      
        self.framePosturas = Frame(self.canvasPosturas,bg='blue')
        self.canvasPosturas.create_window((0, 0), window=self.framePosturas, anchor='nw')

        Label(self.framePosturas,text="Posturas",bg='black',fg='lightblue',font=("arial",10),width=20,justify=LEFT).grid(row=0, column=0, sticky='news')   #.place(x=19,y=18  + altoOtrosDatosPers)
        Label(self.framePosturas,text="Placer",bg='black',fg='lightblue',font=("arial",10),width=6,justify=LEFT).grid(row=0, column=1, sticky='news') 
        Label(self.framePosturas,text="Agotamiento",bg='black',fg='lightblue',font=("arial",10),width=10).grid(row=0, column=2, sticky='news') 

        self.listPersonasPosturas =  []
        self.posturas = [[Entry() for j in range(3)] for i in range(ctdpersonas*(len(self.nombreP)+1))] #+1 es el Persona 1,...
        for p in range(0,ctdpersonas):
            nopers='Persona '+str(p+1)
            Label(self.framePosturas,text=nopers,font=("arial",10), width=20,state="disabled",bg='lightblue').grid(row=p*(len(self.nombreP)+1)+1, column=0, sticky='news')
            a = Persona(nopers)
            self.listPersonasPosturas.append(a)
            rowsI = p*(len(self.nombreP)+1)+1  #+1 titulo, +1 Persona 1,...
            rowsF = rowsI+len(self.nombreP)
            np = 0
            for i in range(rowsI,rowsF):    
                self.posturas[i][0] = Entry(self.framePosturas,font=("arial",10), textvariable=StringVar(value=self.nombreP[np]), width=20,fg='black',state="disabled")
                self.posturas[i][0].grid(row=i+1, column=0, sticky='news')
                self.posturas[i][1] = Entry(self.framePosturas, width=8,justify=CENTER)
                self.posturas[i][1].grid(row=i+1, column=1, sticky='news')
                self.posturas[i][2] = Entry(self.framePosturas, width=13,justify=CENTER)
                self.posturas[i][2].grid(row=i+1, column=2, sticky='news')
                np = np + 1

    def datosEntrada(self):
        self.minimizar = IntVar() 
        Label (text="Desea :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=60)

        Radiobutton(text="Maximizar",bg="lightblue",font=("arial",10), variable=self.minimizar, value=1).place(x=90,y=60)
        Radiobutton(text="Minimizar",bg="lightblue",fg="black",font=("arial",10), variable=self.minimizar, value=2).place(x=200,y=60)

        Label(text="Criterio :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=90)
        self.criterio = StringVar(value='1')
        Radiobutton(text="Tiempo",bg="lightblue",fg="black",font=("arial",10), variable=self.criterio, value='1').place(x=90,y=90)

        Label (text="Restricciones :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=120)
        self.TodosVivos = IntVar(value=1) 
        self.TodosOrgasmo = IntVar(value=1)
        Checkbutton(text="Todos Vivos",bg="lightblue",fg="black",font=("arial",10), variable=self.TodosVivos, onvalue=1, offvalue=0).place(x=140,y=120)
        Checkbutton(text="Todos Orgasmo",bg="lightblue",fg="black",font=("arial",10), variable=self.TodosOrgasmo, onvalue=1, offvalue=0).place(x=240,y=120)    

        self.personas = IntVar()
        Label(text="Cantidad de personas :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=150)
        ctdp = Entry(textvariable=self.personas,width=3)
        ctdp.place(x=200,y=150)

        self.button = Button (text='Completar datos',font=("arial",10),width=20,command=self.mostrarTablas)
        self.button.place(x=20,y=190) 

    def reiniciar(self):
        self.umbral_org = None
        self.energia_ini = None
        self.placer_ini = None
        self.personas = 0
        if self.vr != None:
            self.vr.destroy()
        self.datosEntrada()
        self.mostrarTablas()
      
    def mostrarTablas(self):
        if self.personas.get()<1 or  self.personas.get()>4: #quear que esten todos los datos
            MessageBox.showerror('Error','cantidad de personas inválida')
            return
        self.nombreP = self.nombrePini
        self.creaTablas()
        self.button = Button (text='Ejecutar',font=("arial",10),width=20,height=1,command=self.modelo)
        self.button.place(x=190,y=190) 

    def modelo(self):
            listPersonasPosturas, listRestricciones, fo = self.prepararDatos()
            if self.minimizar.get()==0 or len(listRestricciones)==0 or self.personas.get() not in (1,2,3,4):
                MessageBox.showerror("Error!",'Faltan datos o están incorrectos')
            else:
                resultado = EjecutarModelo(self, listPersonasPosturas, listRestricciones, fo)
                self.muestraResultado(resultado)
                muestraGrafica(listPersonasPosturas, resultado)

    def prepararDatos(self):
        #crear lista con los objetos postura        
        for p in range(len(self.listPersonasPosturas)):
            rowsI = p*(len(self.nombreP)+1)+1
            rowsF = rowsI+len(self.nombreP)
            self.listPersonasPosturas[p].energiaInicial = self.datosPersona[p][1].get()
            self.listPersonasPosturas[p].placerInicial = self.datosPersona[p][2].get()
            self.listPersonasPosturas[p].umbralOrgasmo = self.datosPersona[p][3].get()
            self.listPersonasPosturas[p].posturas.clear()
            for i in range(rowsI,rowsF):   
                nuevaP =Postura(self.posturas[i])
                self.listPersonasPosturas[p].posturas.append( nuevaP )
        #poner las funciones objetivo en la lista fo
        fo = [self.datosFO[i][1].get() for i in range(len(self.nombreP))]

        #lista de restricciones seleccionadas
        listRestricciones = []
        if self.TodosVivos.get()==1: 
            listRestricciones.append("TodosVivos") 
        if self.TodosOrgasmo.get()==1: 
            listRestricciones.append("TodosOrgasmo")              
        return self.listPersonasPosturas, listRestricciones, fo

    def muestraResultado(self,resultado):
        self.vr = Toplevel(self.ventana)
        self.vr.title("Resultado") 
        self.vr.geometry("450x140"+"+"+str(420)+"+"+str(10)) 
        self.vr.resizable(0,0)
        self.vr.config(bg="blue", bd=12, relief="sunken")

        listaresultado=  Listbox(self.vr, height=6, width=60, bg="black",fg="white",font=("arial",10))
        listaresultado.place(x=0,y=0)

        if resultado.x is None:
            listaresultado.insert(END ,'RESULTADO INSATISFACIBLE')
        else:
            for i in range(len(resultado.x)):
                a = self.posturas[i+1][0].get()
                b = round(resultado.x[i],3)
                listaresultado.insert(END ,f'El tiempo que hay que dedicarle a la postura {a} es {b}')
        Button (self.ventana,text='Reiniciar',font=("arial",10),width=10,height=1,command=self.reiniciar).place(x=130,y=430)      

    def muestraError(self,i):
        MessageBox.showerror("Error!",f'linea {i} incorrecta') 


    def cargarFichero(self):
        file = FileDialog.askopenfilename(title='Abrir fichero con los datos', initialdir="C:",filetypes=[("Fichero de texto","*.txt")] )
        if not os.path.isfile(file):
                MessageBox.showerror("Error!",'Archivo no existe')  
                return            
        txt = open(file,'r')
        text = txt.read()
        l =text.split('\n')
        for i in range(4):
            valores = l[i].split(',')

            if len(valores)==0: 
                self.muestraError(i)  
                return
            if len(valores)<1:  
                self.muestraError(i)
                return
            if i==0:     #desea   
                self.minimizar.set(value=valores[0])
            elif i==1:   #restricciones  
                if valores[0]=='1':    
                    self.TodosVivos.set(value=1) 
                else: 
                    self.TodosVivos.set(value=0) 
                if len(valores)!=2: 
                    self.muestraError(i )   
                    return
                if valores[1]=='1':    
                    self.TodosOrgasmo.set(value=1)
                else:   
                    self.TodosOrgasmo.set(value=0)
            elif i==2:
                if len(valores)>1: #escribieron sus propias posturas
                    self.nombreP = valores[1:]
                else:
                    self.nombreP = self.nombrePini
            elif i==3:   #criterio
                if valores[0]=='1': self.criterio.set(value='1') 
                else:   
                    self.muestraError(i)
                    return        

        valores = l[5].split(',')  #ctd de personas
        if len(valores)!=1:
            self.muestraError(i)
            return
        self.personas.set(value=valores[0])
        
        self.creaTablas()
        valores = l[4].split(',')
        if len(valores)!=len(self.nombreP):
            self.muestraError(4)
            return
        for i in range(0,len(self.nombreP)):   #poble FO
            self.datosFO[i][1] = Entry(self.frameFO, width=8, textvariable=IntVar(value=valores[i]),justify=CENTER)
            self.datosFO[i][1].grid(row=i+1,column=1,sticky='news')

           
        linea = 6 #saltar linea de ctd de personas que ya se leyo arriba
        ndp=0
        for i in range(linea,self.personas.get() + linea): #caract de personas
            valores = l[i].split(',')
            if len(valores)!=4:
                self.muestraError(i)
                return
            else:                    
                for j in range(1,4): 
                    self.datosPersona[ndp][j] = Entry(self.frameDatosPersona,width=8, textvariable=IntVar(value=valores[j]),justify=CENTER)
                    self.datosPersona[ndp][j].grid(row=ndp+1,column=j,sticky='news')
                ndp += 1           
        rowI=1
        linea += self.personas.get()
        for i in range(self.personas.get()): #posturas por persona
            for j in range(rowI,len(self.nombreP)+rowI):  
                valores = l[linea].split(',')
                if len(valores)!=3:
                    self.muestraError(i)
                    return
                else:            
                    self.posturas[j][1] = Entry(self.framePosturas,width=8, textvariable=IntVar(value=valores[1]),justify=CENTER)
                    self.posturas[j][1].grid(row=j+1,column=1,sticky='news')
                    self.posturas[j][2] = Entry(self.framePosturas,width=13, textvariable=IntVar(value=valores[2]),justify=CENTER)
                    self.posturas[j][2].grid(row=j+1,column=2,sticky='news')
                    linea += 1
            rowI += (len(self.nombreP)+1)
        self.button = Button (text='Ejecutar',font=("arial",10),width=20,height=1,command=self.modelo)
        self.button.place(x=190,y=190) 

def TiempoProgresivo(res):
    if(res is None):
        return 0
    result = [res[0]]
    sum_act = res[0]
    for i in range(len(res)-1):
        sum_act += res[i + 1]
        result.append(sum_act)
    return result
        
        
def muestraGrafica(listaPosturas, resultado):
        tiemo_progresivo = TiempoProgresivo(resultado.x)
        if(type(tiemo_progresivo) == int):
            return
        for i in range(len(listaPosturas)):
            fig, ax = plt.subplots()
            p = [int(x.placer) for x in listaPosturas[i].posturas]
            c = [int(x.agotamiento) for x in listaPosturas[i].posturas]
            p.sort()
            c.sort()
            num_per = i + 1
            plt.title(f'Grafico de Persona {num_per}')
            plt.xlabel('tiempo')
            plt.ylabel('valores')
            plt.plot(tiemo_progresivo, p, label = 'Placer')
            plt.plot(tiemo_progresivo, c, label = 'Agotamiento')
            plt.legend(loc = 'best')
            plt.show()


if __name__ == '__main__':
    app=Raiz()
