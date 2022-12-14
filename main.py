from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from posturas import Postura
from personas import Persona
from modelo import EjecutarModelo
import matplotlib.pyplot as plt 

class Raiz():
    def __init__(self):       
        #crear ventana principal
        self.ventana = Tk()
        self.ventana.title("App-to sexual ideal")
        self.ventana.geometry("400x500"+"+"+str(10)+"+"+str(10)) 
        self.ventana.resizable(1,1)
        self.ventana.config(bg="lightblue",relief="sunken",bd=12) 

        #Label(text="Proyecto Final de PMA  2022\n\n Kevin Talavera Díaz C-311",bg="lightblue",fg="black",font=("arial",12),border=10,justify=CENTER).place(x=220,y=450)
        Label (text="Ingrese los siguientes datos",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=20)
        Button (text='Cargar de Fichero',font=("arial",9),width=15,height=1,command=self.cargarFichero).place(x=250,y=20) 
        self.canvas = None
        self.vr = None
        self.boton = None 
        self.minimizar = None
        self.umbral_org = None
        self.energia_ini = None
        self.placer_ini = None
        self.canvasPosturas = None
        self.canvasDatosPersona = None
        self.listPersonasPosturas = None
        self.TodosVivos = None
        self.TodosOrgasmo = None
        self.personas = None
        self.button = None
        self.vp = None

        self.datosEntrada()

        self.ventana.mainloop() 

    def otrosDatosPersona(self):
        ctdpersonas = self.personas.get()
        alto = 20 * ctdpersonas+40
        altopixel = ctdpersonas * 20 + 40 + 20 + 20
        if self.canvasDatosPersona is not None:
            self.canvasDatosPersona.destroy()
        self.canvasDatosPersona= Canvas(self.ventana,width=343,height=alto-3,bg='lightblue')
        self.canvasDatosPersona.grid(pady=(230,0 ),padx=(20,0))   

        frameDatosPersona = Frame(self.canvasDatosPersona,bg='lightblue')
        self.canvasDatosPersona.create_window((0, 0), window=frameDatosPersona, anchor='nw')
        
        nombreColumnas = ["Personas","energia\ninicial","placer\ninicial","umbral\norgasmo"]
        for i in range(len(nombreColumnas)):
            Label(frameDatosPersona,text=nombreColumnas[i],font=("arial",10),fg='lightblue',bg='black', width=10,height=2 , state="disabled").grid(row=0, column=i, sticky='news')

        self.datosPersona = [[Entry() for j in range(4)] for i in range(self.personas.get())]

        for i in range(0,self.personas.get()):
            nopers='Persona '+str(i+1)
            self.datosPersona[i][0] = Entry(frameDatosPersona,textvariable=StringVar(value=nopers),font=("arial",10), width=10,state="disabled",bg='lightblue',fg='black')
            self.datosPersona[i][0].grid(row=i+1, column=0, sticky='news')

            for j in range(1,4):  
                self.datosPersona[i][j] = Entry(frameDatosPersona, width=8,justify=CENTER)
                self.datosPersona[i][j].grid(row=i+1, column=j, sticky='news')

    def creaCanvasPosturas(self):
        if self.personas.get()<1 or self.personas.get()>4: return
        if self.vp == None:
            self.vp = Toplevel(self.ventana)
            self.vp.title("Datos de las posturas") 
            self.vp.geometry("430x600"+"+"+str(420)+"+"+str(10)) 
            self.vp.resizable(1,1)
            self.vp.config(bg="lightblue", bd=12, relief="sunken")
        else:
            self.canvasPosturas.destroy()

        ctdpersonas = self.personas.get()
        alto = 20*6 * ctdpersonas
        altopixel = ctdpersonas * 6 * 20 + 40 + 20 + 20
        self.vp.geometry("500x"+str(altopixel)+"+"+str(420)+"+"+str(10)) 
        self.canvasPosturas= Canvas(self.vp,width=370,height=alto,bg='lightblue')
        self.canvasPosturas.grid(pady=(40,0 ),padx=(20,0))      
        frame_posturas = Frame(self.canvasPosturas,bg='lightblue')
        self.canvasPosturas.create_window((0, 0), window=frame_posturas, anchor='nw')
        Label(self.vp,text="Posturas",bg='black',fg='lightblue',font=("arial",10),width=20,justify=LEFT).place(x=19,y=18)
        Label(self.vp,text="Placer",bg='black',fg='lightblue',font=("arial",10),width=6,justify=LEFT).place(x=186,y=18)
        Label(self.vp,text="Agotamiento",bg='black',fg='lightblue',font=("arial",10),width=10).place(x=235,y=18)
        Label(self.vp,text=self.criterio.get(),bg='black',fg='lightblue',font=("arial",10),width=9).place(x=320,y=18)

        rows = 6
        columns = 4
        nombreP=['misionero','perrito','69','yunque','rueda']
        self.listPersonasPosturas =  []
        self.posturas = [[Entry() for j in range(columns)] for i in range(ctdpersonas*rows)]
        for p in range(0,ctdpersonas):
            nopers='Persona '+str(p+1)
            Label(frame_posturas,text=nopers,font=("arial",10), width=20,state="disabled",bg='lightblue').grid(row=p*6, column=0, sticky='news')
            a = Persona(nopers)
            self.listPersonasPosturas.append(a)
            rowsI = p*6+1
            rowsF = rowsI+5
            np = 0
            for i in range(rowsI,rowsF):    
                        self.posturas[i][0] = Entry(frame_posturas,font=("arial",10), textvariable=StringVar(value=nombreP[np]), width=20,fg='black',state="disabled")
                        self.posturas[i][0].grid(row=i, column=0, sticky='news')
                        self.posturas[i][1] = Entry(frame_posturas, width=8,justify=CENTER)
                        self.posturas[i][1].grid(row=i, column=1, sticky='news')
                        self.posturas[i][2] = Entry(frame_posturas, width=13,justify=CENTER)
                        self.posturas[i][2].grid(row=i, column=2, sticky='news')
                        if p==0:
                            self.posturas[i][3] = Entry(frame_posturas, width=12,justify=CENTER,bg='black',fg='lightblue')
                            self.posturas[i][3].grid(row=i, column=5, sticky='news')
                        np = np + 1
        self.otrosDatosPersona()


    def datosEntrada(self):
        self.minimizar = IntVar() 
        Label (text="Desea :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=60)
        Radiobutton(text="Maximizar",bg="lightblue",font=("arial",10), variable=self.minimizar, value=0).place(x=90,y=60)
        Radiobutton(text="Minimizar",bg="lightblue",fg="black",font=("arial",10), variable=self.minimizar, value=1).place(x=200,y=60)

        Label(text="Criterio :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=90)
        self.criterio = StringVar(value='Tiempo')
        Radiobutton(text="Tiempo",bg="lightblue",fg="black",font=("arial",10), variable=self.criterio, value='Tiempo').place(x=200,y=90)

        Label (text="Restricciones :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=120)
        self.TodosVivos = IntVar(value=1) 
        self.TodosOrgasmo = IntVar(value=1)
        Checkbutton(text="Todos Vivos",bg="lightblue",fg="black",font=("arial",10), variable=self.TodosVivos, onvalue=1, offvalue=0).place(x=140,y=120)
        Checkbutton(text="Todos Orgasmo",bg="lightblue",fg="black",font=("arial",10), variable=self.TodosOrgasmo, onvalue=1, offvalue=0).place(x=240,y=120)    

        self.personas = IntVar()
        Label(text="Cantidad de personas :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=150)
        ctdp = Entry(textvariable=self.personas,width=3)
        ctdp.place(x=200,y=150)
        #ctdp.bind('<FocusOut>', lambda event: self.creaCanvasPosturas())

        self.button = Button (text='Introducir datos de las personas',font=("arial",10),width=30,command=self.introducir)
        self.button.place(x=80,y=190) 


    def reiniciar(self):
        self.umbral_org = None
        self.energia_ini = None
        self.placer_ini = None
        self.personas = 0
        if self.vr != None:
            self.vr.destroy()    
        self.datosEntrada()
        
    def cargarFichero(self):
        ruta = FileDialog.askopenfilename(title='Abrir fichero con los datos', initialdir="C:",filetypes=[("Fichero de texto","*.txt")] )
        #cargar
        
    def introducir(self):
        if self.personas.get()<1 or  self.personas.get()>4: #quear que esten todos los datos
            MessageBox.showerror('Error','cantidad de personas inválida')
            return
        if self.listPersonasPosturas==None:
            self.creaCanvasPosturas()
            self.button = Button (text='Ejecutar',font=("arial",10),width=20,height=1,command=self.modelo)
            self.button.place(x=130,y=350) 

    def modelo(self):
            Label(text="Espere    ...",bg="lightblue",fg="black",font=("arial",10),width=20,height=2).place(x=130,y=330)
            listPersonasPosturas, listRestricciones, fo = self.prepararDatos()
            resultado = EjecutarModelo(self, listPersonasPosturas, listRestricciones, fo)
            self.muestraResultado(resultado)
            muestraGrafica(listPersonasPosturas, resultado)

    def prepararDatos(self):
        #crear lista con los objetos postura
        for p in range(len(self.listPersonasPosturas)):
            rowsI = p*6+1
            rowsF = rowsI+5
            self.listPersonasPosturas[p].energiaInicial = self.datosPersona[p][1].get()
            self.listPersonasPosturas[p].placerInicial = self.datosPersona[p][2].get()
            self.listPersonasPosturas[p].umbralOrgasmo = self.datosPersona[p][3].get()
            for i in range(rowsI,rowsF):   
                nuevaP =Postura(self.posturas[i])
                self.listPersonasPosturas[p].posturas.append( nuevaP )
        #poner las funciones objetivo en la lista fo
        fo = [self.listPersonasPosturas[0].posturas[i].fo for i in range(5)]
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
        self.vr.geometry("450x150"+"+"+str(420)+"+"+str(10)) 
        self.vr.resizable(0,0)
        self.vr.config(bg="blue", bd=12, relief="sunken")

        listaresultado=  Listbox(self.vr, height=6, width=60, bg="black",fg="white",font=("arial",10))
        listaresultado.place(x=0,y=0)

        if resultado.x is None:
            listaresultado.insert(END ,'RESULTADO INSATISFACIBLE')
        else:
            for i in range(len(resultado.x)):
                listaresultado.insert(END ,f'El tiempo que hay que dedicarle a la postura {self.posturas[i][0].get()} es {round(resultado.x[i],3)}')
        Button (self.ventana,text='Reiniciar',font=("arial",10),width=10,height=1,command=self.reiniciar).place(x=130,y=430)      

def TiempoProgresivo(res):
    result = [res[0]]
    sum_act = res[0]
    for i in range(len(res)-1):
        sum_act += res[i + 1]
        result.append(sum_act)
    return result
        
        
def muestraGrafica(listaPosturas, resultado):
        tiemo_progresivo = TiempoProgresivo(resultado.x)
        for i in range(len(listaPosturas)):
            fig, ax = plt.subplots()
            p = [int(x.placer) for x in listaPosturas[i].posturas]
            c = [int(x.agotamiento) for x in listaPosturas[i].posturas]
            p.sort()
            c.sort()
            plt.plot(tiemo_progresivo, p, label = 'Placer')
            plt.plot(tiemo_progresivo, c, label = 'Agotamiento')
            plt.legend(loc = 'best')
            plt.show()


if __name__ == '__main__':

    app=Raiz()
