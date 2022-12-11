from tkinter import *
from posturas import *
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
        Label (text="Ingrese los siguientes datos",bg="lightblue",fg="black",font=("arial",12)).place(x=70,y=20)

        self.canvas = None
        self.vr = None
        self.boton = None 
        self.minimizar = None
        self.umbral_org = None
        self.energia_ini = None
        self.placer_ini = None
        self.canvasPosturas = None
        self.posturas = None
        self.TodosVivos = None
        self.TodosOrgasmo = None

        self.datosEntrada()

        self.ventana.mainloop() 

    def creaCanvasPosturas(self):

        self.canvasPosturas= Canvas(self.ventana,width=324,height=95)
        self.canvasPosturas.grid(pady=(290,0 ),padx=(20,0))      
        frame_posturas = Frame(self.canvasPosturas)
        self.canvasPosturas.create_window((0, 0), window=frame_posturas, anchor='nw')
        Label(text="Posturas",font=("arial",10),width=17,justify=LEFT).place(x=20,y=267)
        Label(text="Placer",font=("arial",10),width=6,justify=LEFT).place(x=164,y=267)
        Label(text="Agotamiento",font=("arial",10),width=9).place(x=220,y=267)
        Label(text="Tiempo",font=("arial",10),width=5).place(x=300,y=267)
        rows = 5
        columns = 4
        posturas =None
        posturas = [[Entry() for j in range(columns)] for i in range(rows)]
        list=['misionero','perrito','69','yunque','rueda']
        listIntvar = []
        for i in range(0, rows):
                listIntvar.append(StringVar(value=list[i]))
                posturas[i][0] = Entry(frame_posturas,font=("arial",10),textvariable=listIntvar[i], width=20,state="readonly")
                posturas[i][0].grid(row=i, column=0, sticky='news')
                posturas[i][1] = Entry(frame_posturas, width=8,justify=CENTER)
                posturas[i][1].grid(row=i, column=1, sticky='news')
                posturas[i][2] = Entry(frame_posturas, width=13,justify=CENTER)
                posturas[i][2].grid(row=i, column=2, sticky='news')
                posturas[i][3] = Entry(frame_posturas, width=8,justify=CENTER)
                posturas[i][3].grid(row=i, column=3, sticky='news')
        return posturas

    def datosEntrada(self):

        if self.canvasPosturas != None:
            self.canvasPosturas.destroy()
        self.posturas=self.creaCanvasPosturas()

        self.minimizar = IntVar() 
        Label (text="Desea :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=60)
        Radiobutton(text="Maximizar",bg="lightblue",font=("arial",10), variable=self.minimizar, value=0).place(x=90,y=60)
        Radiobutton(text="Minimizar",bg="lightblue",fg="black",font=("arial",10), variable=self.minimizar, value=1).place(x=200,y=60)

        Label(text="Criterio :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=90)
        self.criterio = IntVar(value=1)
        Radiobutton(text="Tiempo",bg="lightblue",fg="black",font=("arial",10), variable=self.criterio, value='1').place(x=200,y=90)

        self.umbral_org = IntVar()
        Label(text="Umbral del orgasmo :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=120)
        Entry(textvariable=self.umbral_org,width=3).place(x=200,y=120)

        self.energia_ini = IntVar()
        Label(text="Energía inicial :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=150)
        Entry(textvariable=self.energia_ini,width=3).place(x=200,y=150)

        self.placer_ini = IntVar()
        Label(text="Placer inicial ",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=180)
        Entry(textvariable=self.placer_ini,width=3).place(x=200,y=180)

        Label (text="Restricciones :",bg="lightblue",fg="black",font=("arial",12)).place(x=20,y=210)
        self.TodosVivos = IntVar(value=1) 
        self.TodosOrgasmo = IntVar(value=1)
        Checkbutton(text="Todos Vivos",bg="lightblue",fg="black",font=("arial",10), variable=self.TodosVivos, onvalue=1, offvalue=0).place(x=140,y=210)
        Checkbutton(text="Todos Orgasmo",bg="lightblue",fg="black",font=("arial",10), variable=self.TodosOrgasmo, onvalue=1, offvalue=0).place(x=240,y=210)

        Button (text='Ejecutar',font=("arial",10),width=10,height=1,command=self.modelo).place(x=130,y=430)      

    def reiniciar(self):
        self.umbral_org = None
        self.energia_ini = None
        self.placer_ini = None
        if self.vr != None:
            self.vr.destroy()    
        self.datosEntrada()

    def modelo(self):
        Label(text="Espere    ...",bg="lightblue",fg="black",font=("arial",10),width=20,height=2).place(x=130,y=430)
        listPosturas, listRestricciones, fo = self.prepararDatos()
        resultado = EjecutarModelo(self, listPosturas, listRestricciones, fo)
        self.muestraResultado(resultado)
        muestraGrafica(listPosturas, resultado)

    def prepararDatos(self):
        #crear lista con los objetos postura
        listPosturas = []
        for i in range(len(self.posturas)):
            listPosturas.append( Postura(self.posturas[i]) )
        #poner las funciones objetivo en la lista fo
        fo = [listPosturas[i].tiempo for i in range(len(listPosturas))]
        #lista de restricciones seleccionadas
        listRestricciones = []
        if self.TodosVivos.get()==1: 
            listRestricciones.append("TodosVivos") 
        if self.TodosOrgasmo.get()==1: 
            listRestricciones.append("TodosOrgasmo")  
        return listPosturas, listRestricciones, fo

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

def muestraGrafica(listaPosturas, resultado):
        fig, ax = plt.subplots()
        p = [x.placer for x in listaPosturas]
        c = [x.agotamiento for x in listaPosturas]
        plt.plot(resultado.x, p, label = 'Placer')
        plt.plot(resultado.x, c, label = 'Agotamiento')
        ax.legend(loc = 'best')
        plt.show()

if __name__ == '__main__':
    app=Raiz()
