from numpy import absolute
from xml.dom import minidom
from graphviz import Graph
from os import startfile
import graphviz
from os import system
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from Ciudad import *
from Fila import *
import Esstructura_ciudades
import Estructuras_filas


lista_ciudades = Esstructura_ciudades.ListaDoble()


def menu(): 
    salir = False
  
    while salir != True:    
        #AQUI ESTA EL MENU PRINCIPAL    
        print("")
        print("--------------------------------------------------------------------")
        print("1. CARGAR XML")
        print("2. MOSTRAR CIUDADES Y ELEGIR ")
        print("3. VER PATRON ELEGIDO")
        print("4. ELEGIR NUEVO PATRON")
        print("5. REALIZAR CAMBIOS")
        print("6. VER NUEVO PATRON")
        print("7. SALIR")
        print("--------------------------------------------------------------------")
        print("")
        opcion = int(input("DIGITE EL NUMERO DE LA OPCION CORRESPONDIENTE "))
        
        
        if(opcion == 1):
            print("AQUI SE SELECCIONAN LOS DATOS ")
            print("")
            nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
            
            doc = minidom.parse(nombrearch)
            ciudades = doc.getElementsByTagName("ciudad")

            for ciudad in ciudades:
                
                nombre = ciudad.getElementsByTagName("nombre")[0]
                nom = nombre.firstChild.data
                cant_filas = 0
                cant_columnas = 0
                print(nom)
                
                for node in ciudad.getElementsByTagName("nombre"):
                    cant_filas = node.getAttribute("filas")
                    print(cant_filas)
                    cant_columnas = node.getAttribute("columnas")
                    print(cant_columnas)
                
                filas = ciudad.getElementsByTagName('fila')
                lista_filas = Estructuras_filas.ListaDoble_fila()
                for fila in filas:
                    numero = fila.attributes['numero'].value 
                    lista_letras = fila.childNodes[0].data
                    #print(codigo_pat)
                    #print(patron.childNodes[0].data)
                    fila_nueva = Fila(numero, lista_letras)
                    lista_filas.añadirNodoPrincipio(fila_nueva)

                ciudad_nueva = Ciudad(nom,cant_filas, cant_columnas,lista_filas)
                lista_ciudades.añadirNodoPrincipio(ciudad_nueva)
                               
                print("")
            print("LISTA DE CIUDADES ")
            lista_ciudades.imprimirLista()


def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  

    