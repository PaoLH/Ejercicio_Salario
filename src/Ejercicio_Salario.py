from flask import Flask
import tkinter as tk
import os
import sys


app = Flask(__name__)
@app.route("/")

#Función para hacer la resta del salario y gasto
def resta():
    resta=int(salario.get())-int(gasto.get())
    #Condiciones para definir el color del cliente
    if resta>7000:
        e3=tk.Label(ventana,textvariable=var,bg='blue',fg='white')
        e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
    elif resta>3000 and resta<=7000:
        e3=tk.Label(ventana,textvariable=var,bg='green',fg='white')
        e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
    elif resta>1000 and resta<=3000:
        e3=tk.Label(ventana,textvariable=var,bg='yellow',fg='black')
        e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
    elif resta<=1000:
        e3=tk.Label(ventana,textvariable=var,bg='red',fg='white')
        e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
    
    return var.set(resta)

#Función para reiniciar app 
def reset():
    os.execl(sys.executable, sys.executable, * sys.argv) 
    
#Función para cerrar
def cerrar():
    ventana.destroy()
    
    
#Configuración de la ventana 
ventana=tk.Tk()
ventana.title("Salario")
ventana.geometry('280x280')
ventana.configure(bg='bisque')
var=tk.StringVar()

#Texto de salario y entrada de datos
e1=tk.Label(ventana,text="Salario: ", bg='papaya whip', fg='black')
e1.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
salario=tk.Entry(ventana)
salario.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

#Texto de gasto y entrada de datos
e2=tk.Label(ventana,text="Gasto: ", bg='papaya whip', fg='black')
e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
gasto=tk.Entry(ventana)
gasto.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

#Botón para realizar la resta 
botonresta=tk.Button(ventana,text="Color del cliente",fg="black",command=resta)
botonresta.pack(side=tk.TOP)

#Botón para reiniciar
botonreset=tk.Button(ventana, text="Reset",fg='black',command=reset)
botonreset.pack(padx=4,pady=4,ipadx=4,ipady=4,side=tk.LEFT)

#Botón para finalizar
botoncerrar=tk.Button(ventana,text="Cerrar",fg="black",command=cerrar)
botoncerrar.pack(padx=4,pady=4,ipadx=4,ipady=4,side=tk.RIGHT)


ventana.mainloop()