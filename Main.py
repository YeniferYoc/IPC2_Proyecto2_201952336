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
from Robot import *
import Esstructura_ciudades
import Estructuras_filas
import Estructuras_robot
import Estructura_unidad_mili
from Unidad_militar import *


lista_ciudades = Esstructura_ciudades.ListaDoble()
lista_robots = Estructuras_robot.ListaDoble_robot()


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
                nodo_temporal = Esstructura_ciudades.Nodo('')
                nodo_temporal = lista_ciudades.head
                cant_filas = 0
                cant_columnas = 0

                if nodo_temporal == None:#SI LA LISTA ESTA VACIA NO HAY NADA QUE VERIFICAR
                    print("la lista esta vacia ")
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
                        fila_nueva = Fila(numero, lista_letras)
                        lista_filas.añadirNodoPrincipio(fila_nueva)

                    unidadMilitares = ciudad.getElementsByTagName('unidadMilitar')
                    lista_unidades = Estructura_unidad_mili.ListaDoble_unidad()
                    for unidad in unidadMilitares:
                        fila_u = unidad.attributes['fila'].value
                        columna_u = unidad.attributes['columna'].value
                        capacidad_u = unidad.childNodes[0].data
                        unidad_nueva = Unidad_militar(fila_u, columna_u, capacidad_u)
                        lista_unidades.añadirNodoPrincipio(unidad_nueva)

                    ciudad_nueva = Ciudad(nom,cant_filas, cant_columnas,lista_filas,lista_unidades)
                    lista_ciudades.añadirNodoPrincipio(ciudad_nueva)
                    
                
                else: #SI LA LISTA TIENE ALGO ENTONCES HAY QUE EVALUARLA
                    repetido = False
                    while nodo_temporal != None:
                        if nom == nodo_temporal.objeto_ciudad.nombre:
                            print("si es repetido"+nom)
                            for node in ciudad.getElementsByTagName("nombre"):
                                #SOBREESCRIBIMOS LOS DATOS DE CANTIDAD FILAS Y COLUMNAS
                                nodo_temporal.objeto_ciudad.cant_filas = node.getAttribute("filas")
                                nodo_temporal.objeto_ciudad.cant_columnas = node.getAttribute("columnas")
                            #SOBREESCRIBIMOS LA LISTA DE LAS FILAS
                            filas2 = ciudad.getElementsByTagName('fila')
                            lista_filas_sobre = Estructuras_filas.ListaDoble_fila()
                            for fila in filas2:
                                numero_sobre = fila.attributes['numero'].value 
                                lista_letras_sobre = fila.childNodes[0].data
                                fila_nueva_sobre = Fila(numero_sobre, lista_letras_sobre)
                                lista_filas_sobre.añadirNodoPrincipio(fila_nueva_sobre)
                            nodo_temporal.objeto_ciudad.filas = lista_filas_sobre
                            repetido = True
                            
                            unidadMilitares2 = ciudad.getElementsByTagName('unidadMilitar')
                            lista_unidades_sobres = Estructura_unidad_mili.ListaDoble_unidad()
                            for unidad in unidadMilitares2:
                                fila_u2 = unidad.attributes['fila'].value
                                columna_u2 = unidad.attributes['columna'].value
                                capacidad_u2 = unidad.childNodes[0].data
                                unidad_nueva_sobres = Unidad_militar(fila_u2, columna_u2, capacidad_u2)
                                lista_unidades_sobres.añadirNodoPrincipio(unidad_nueva_sobres)
                            nodo_temporal.objeto_ciudad.unidades_militares = lista_unidades_sobres
                                    
                            break
                        nodo_temporal = nodo_temporal.siguiente
                    if repetido == True:
                        pass
                    else: 
                            print("esta en el else "+nom)
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
                                fila_nueva = Fila(numero, lista_letras)
                                lista_filas.añadirNodoPrincipio(fila_nueva)
                            
                            unidadMilitares = ciudad.getElementsByTagName('unidadMilitar')
                            lista_unidades = Estructura_unidad_mili.ListaDoble_unidad()
                            for unidad in unidadMilitares:
                                fila_u = unidad.attributes['fila'].value
                                columna_u = unidad.attributes['columna'].value
                                capacidad_u = unidad.childNodes[0].data
                                unidad_nueva = Unidad_militar(fila_u, columna_u, capacidad_u)
                                lista_unidades.añadirNodoPrincipio(unidad_nueva)

                            ciudad_nueva = Ciudad(nom,cant_filas, cant_columnas,lista_filas,lista_unidades)
                            lista_ciudades.añadirNodoPrincipio(ciudad_nueva)
                    
                ######################################################
                '''for node in ciudad.getElementsByTagName("nombre"):
                    cant_filas = node.getAttribute("filas")
                    print(cant_filas)
                    cant_columnas = node.getAttribute("columnas")
                    print(cant_columnas)
                
                filas = ciudad.getElementsByTagName('fila')
                lista_filas = Estructuras_filas.ListaDoble_fila()
                for fila in filas:
                    numero = fila.attributes['numero'].value 
                    lista_letras = fila.childNodes[0].data
                    fila_nueva = Fila(numero, lista_letras)
                    lista_filas.añadirNodoPrincipio(fila_nueva)

                ciudad_nueva = Ciudad(nom,cant_filas, cant_columnas,lista_filas)
                lista_ciudades.añadirNodoPrincipio(ciudad_nueva)'''
                               
                print("")
            print("LISTA DE CIUDADES ")
            lista_ciudades.imprimirLista()
            
            ############################## ROBOTS ##############################

            robots = doc.getElementsByTagName("robot")
            for robot in robots:
                
                nombre = robot.getElementsByTagName("nombre")[0]
                nom = nombre.firstChild.data
                tipo = ""
                capacidad = 0
                nodo_temporal_rob = Estructuras_robot.Nodo('')
                nodo_temporal_rob = lista_robots.head
                if nodo_temporal_rob == None: #la lista esta vacia
                    print("la lista esta vacia")
                    for node in robot.getElementsByTagName("nombre"):
                        tipo = node.getAttribute("tipo")
                        
                        capacidad = node.getAttribute("capacidad")
                        

                    robot_nuevo = Robot(nom, tipo, capacidad)
                    lista_robots.añadirNodoPrincipio(robot_nuevo)
                
                else: #la lista tiene algo dentro 
                    robot_repetido = False
                    while nodo_temporal_rob != None:
                        if nom == nodo_temporal_rob.objeto_robot.nombre:
                            robot_repetido = True
                            for node in robot.getElementsByTagName("nombre"):
                                nodo_temporal_rob.objeto_robot.tipo = node.getAttribute("tipo")
                                
                                nodo_temporal_rob.objeto_robot.capacidad = node.getAttribute("capacidad")

                        nodo_temporal_rob = nodo_temporal_rob.siguiente

                    if robot_repetido == True:
                        pass
                    else: 
                        for node in robot.getElementsByTagName("nombre"):
                            tipo = node.getAttribute("tipo")
                            
                            capacidad = node.getAttribute("capacidad")
                            

                        robot_nuevo = Robot(nom, tipo, capacidad)
                        lista_robots.añadirNodoPrincipio(robot_nuevo)
                  
            print("")
            print("LISTA DE ROBOTS")
            lista_robots.imprimirLista()


def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  

    