#app para convertir pies a metros usando Tkinter.
#Beltran Alison Judith
#23 Febrero 2023.

from tkinter import*
from tkinter import ttk

class Conversor:

    #tipo constructor de la clase
    def __init__(self, raiz):

        raiz.title("Pies a Metros")

        self.pies=StringVar()
        self.metros=StringVar()

        mainFrame=ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0)

        piesEntry=ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2,row=2)
        
        #Hcer que funcione con enter
        raiz.bind("<Return>", self.calcular)
    
    def calcular(self, *args):
        print("Boton Presionado")
        piesUsuario = float(self.pies.get()) #siempre devuelve la cadena.
        print("Pies ingresados: ", piesUsuario)
        piesFlotate = float(piesUsuario) #Conversion de cadena a flotante.
        metros= piesFlotate*0.3048
        print("Pies ingresados: ", piesUsuario)
        print("Metros: ",metros)
        self.metros.set(metros)

    if __name__=="__main__":
        print("Este es el archivo Principal. ")
        print("Nada mas se mostrara esto si es el Principal")

 #   self.pies=StringVar()
 #   self.metros=StringVar()

 #   mainframe=ttk.Frame(raiz, padding="3 3 12 12")
 #   mainframe.grind(column=2, row=1, sticky=(W, E))

