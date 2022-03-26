from numpy import absolute, rec
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
from Celda import *
import Esstructura_ciudades
import Estructuras_filas
import Estructuras_robot
import Estructura_unidad_mili
import Estructuras_celda
from Unidad_militar import *


lista_ciudades = Esstructura_ciudades.ListaDoble()
lista_robots = Estructuras_robot.ListaDoble_robot()
ciudad_elegida = None
celda_rescatar  = None
robot_elegido = None


def menu(): 
    salir = False
  
    while salir != True:    
        #AQUI ESTA EL MENU PRINCIPAL    
        print("")
        print("--------------------------------------------------------------------")
        print("1. CARGAR XML")
        print("2. ELEGIR MISION")
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
                    #print("la lista esta vacia ")
                    for node in ciudad.getElementsByTagName("nombre"):
                        cant_filas = node.getAttribute("filas")
                        #print(cant_filas)
                        cant_columnas = node.getAttribute("columnas")
                        #print(cant_columnas)
                    
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
                            #print("si es repetido"+nom)
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
                            #print("esta en el else "+nom)
                            for node in ciudad.getElementsByTagName("nombre"):
                                cant_filas = node.getAttribute("filas")
                                #print(cant_filas)
                                cant_columnas = node.getAttribute("columnas")
                                #print(cant_columnas)
                            
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
            #print("LISTA DE CIUDADES ")
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
                    #print("la lista esta vacia")
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
                  
            #print("")
            #print("LISTA DE ROBOTS")
            lista_robots.imprimirLista()
        
        if(opcion == 2):
            print("")
            print("----------------------------------------------------------")
            print("|\t \t AQUI SE ELIGE LA MISION\t \t |")
            print("|\t \t\t \t \t \t \t | ")
            print("|\t \t 1. MISION DE RESCATE\t \t \t |")
            print("|\t \t 2. MISION DE EXTRACCION DE RECURSOS\t |")
            print("----------------------------------------------------------")
            print("")
            opcion_mision = int(input("QUE TIPO DE MISION DESEA REALIZAR: "))

            if opcion_mision == 1:
                arreglo = Seleccionar_ciudad_celda('C','ChapinRescue', lista_ciudades, lista_robots )
                print("")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° RESUMEN DE MISION °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                ciudad_ = arreglo[0]
                celda_ = arreglo[1]
                robot_ = arreglo[2]
                print("-----------------------------> CIUDAD: \t"+ciudad_.nombre)
                print("-----------------------------> CELDA A RESCATAR: ")
                celda_.mostrar_celda()
                print("-----------------------------> ROBOT ENCARGADO: ")
                robot_.mostrar_robot()
                '''lista_tienen_rescate = buscar_ciudades('C', lista_ciudades)
                lista_hay_robot = buscar_robot('ChapinRescue', lista_robots)
                
                nodo_tem_tienen = Esstructura_ciudades.Nodo('')
                nodo_tem_tienen = lista_tienen_rescate.head
                
                nodo_tem_rob = Estructuras_robot.Nodo('')
                nodo_tem_rob = lista_hay_robot.head

                if nodo_tem_tienen != None and nodo_tem_rob != None:
                    print("ESTAS CIUDADES TIENEN UNIDAD CIVIL DE RESCATE: ")
                    print("")
                    contador = 0
                    contador_rob = 0
                    while nodo_tem_tienen != None:
                        contador += 1
                        print("\t -----> "+str(contador)+" "+nodo_tem_tienen.objeto_ciudad.nombre)
                        
                        nodo_tem_tienen = nodo_tem_tienen.siguiente
                        print("")
                    print("Y ESTOS SON LOS ROBOTS DISPONIBLES: ")
                    while nodo_tem_rob != None:
                        contador_rob += 1
                        print("\t -----> "+str(contador_rob)+" "+nodo_tem_rob.objeto_robot.nombre)  
                        nodo_tem_rob = nodo_tem_rob.siguiente
                    print("")
                    if contador == 1:
                                print("PUESTO QUE SOLO HAY UNA CIUDAD LA MISION SE LLEVARA ACABO EN ESTA")
                                nodo_tem_tienen = lista_tienen_rescate.head
                                ciudad_elegida = nodo_tem_tienen.objeto_ciudad
                                lista_celdas = lista_rescates('C', nodo_tem_tienen.objeto_ciudad)
                                print(nodo_tem_tienen.objeto_ciudad.nombre)
                                nodo_celda = Estructuras_celda.Nodo('')
                                nodo_celda = lista_celdas.head
                                contador_celdas = 0
                                while nodo_celda != None:
                                    contador_celdas += 1
                                    print(str(contador_celdas)+". --->"+"FILA: "+str(nodo_celda.objeto_celda.fila)+", COLUMNA: "+str(nodo_celda.objeto_celda.columna))
                                    nodo_celda = nodo_celda.siguiente
                                if contador_celdas == 1:
                                    print("SOLO HAY UNA UNIDAD A RESCATAR ASI QUE LA MISION SE LLEVARA A CABO EN ESTA")
                                    nodo_celda = lista_celdas.head
                                    celda_rescatar  = nodo_celda.objeto_celda
                                    

                                else: 
                                    opcion_celda = int(input("ELIJA LA UNIDAD QUE DESEA RESCATAR: "))
                                    contador_celda_ele = 0
                                    nodo_celda = lista_celdas.head
                                    while nodo_celda != None:
                                        contador_celda_ele += 1
                                        if contador_celda_ele == opcion_celda:
                                            celda_rescatar = nodo_celda.objeto_celda
                                        nodo_celda = nodo_celda.siguiente
                        
                    else:
                        opcion_ciudad = int(input("ELIJA EL NUMERO DE CIUDAD DONDE DESEA REALIZAR LA MISION: "))
                        contador_ciu_ele = 0
                        nodo_tem_tienen = lista_tienen_rescate.head
                        while nodo_tem_tienen != None:
                            contador_ciu_ele += 1
                            if contador_ciu_ele == opcion_ciudad:
                                ciudad_elegida = nodo_tem_tienen.objeto_ciudad
                                lista_celdas = lista_rescates('C', nodo_tem_tienen.objeto_ciudad)
                                print(nodo_tem_tienen.objeto_ciudad.nombre)
                                nodo_celda = Estructuras_celda.Nodo('')
                                nodo_celda = lista_celdas.head
                                contador_celdas = 0
                                while nodo_celda != None:
                                    contador_celdas += 1
                                    print(str(contador_celdas)+". --->"+"FILA: "+str(nodo_celda.objeto_celda.fila)+", COLUMNA: "+str(nodo_celda.objeto_celda.columna))
                                    nodo_celda = nodo_celda.siguiente
                                if contador_celdas == 1:
                                    print("SOLO HAY UNA UNIDAD A RESCATAR ASI QUE LA MISION SE LLEVARA A CABO EN ESTA")
                                    nodo_celda = lista_celdas.head
                                    celda_rescatar  = nodo_celda.objeto_celda

                                else: 
                                    opcion_celda = int(input("ELIJA LA UNIDAD QUE DESEA RESCATAR: "))
                                    contador_celda_ele = 0
                                    nodo_celda = lista_celdas.head
                                    while nodo_celda != None:
                                        contador_celda_ele += 1
                                        if contador_celda_ele == opcion_celda:
                                            celda_rescatar = nodo_celda.objeto_celda
                                        nodo_celda = nodo_celda.siguiente

                                #lista_celdas.imprimirLista()
                            
                            nodo_tem_tienen = nodo_tem_tienen.siguiente
                            print("")

                    print(ciudad_elegida.nombre)
                    celda_rescatar.mostrar_celda()

                    if contador_rob == 1:
                        print("SOLO HAY UN ROBOT ENTONCES ESTE EJECUTARA LA MISION")
                        nodo_tem_rob = lista_hay_robot.head
                        robot_elegido = nodo_tem_rob.objeto_robot
                    else:
                        opcion_rob_ele = int(input(" ELIJA EL ROBOT QUE LLEVARA A CABO LA MISION: "))
                        contador_rob_ele = 0
                        nodo_tem_rob = lista_hay_robot.head
                        while nodo_tem_rob != None:
                            contador_rob_ele += 1
                            if contador_rob_ele == opcion_rob_ele:
                                robot_elegido = nodo_tem_rob.objeto_robot
                            nodo_tem_rob = nodo_tem_rob.siguiente
                        
                    print("")
                    robot_elegido.mostrar_robot()
  
                else:
                    print("NO SE PUEDE REALIZAR ESTA MISION PORQUE NO HAY LOS RECURSOS DISPONIBLES")'''
                

            if opcion_mision == 2:############################### AQUI VA LA MISION 2
                arreglo2 = Seleccionar_ciudad_celda('R','ChapinFighter', lista_ciudades, lista_robots )
                print("")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° RESUMEN DE MISION °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                ciudad_ = arreglo2[0]
                celda_ = arreglo2[1]
                robot_ = arreglo2[2]
                print("------------> CIUDAD: \t"+ciudad_.nombre)
                print("------------> CELDA A RESCATAR: ")
                celda_.mostrar_celda()
                print("------------> ROBOT ENCARGADO: ")
                robot_.mostrar_robot()
                
                
def Seleccionar_ciudad_celda(tipo_celda, tipo_robot, lista_ciudadess, lista_robotss):
                lista_tienen_rescate = buscar_ciudades(tipo_celda, lista_ciudadess)
                lista_hay_robot = buscar_robot(tipo_robot, lista_robotss)
                        
                nodo_tem_tienen = Esstructura_ciudades.Nodo('')
                nodo_tem_tienen = lista_tienen_rescate.head
                            
                nodo_tem_rob = Estructuras_robot.Nodo('')
                nodo_tem_rob = lista_hay_robot.head
                arreglo_ciudad_celda_rob = [None, None, None]
                if nodo_tem_tienen != None and nodo_tem_rob != None:
                    print("ESTAS CIUDADES TIENEN UNIDADES A RESCATAR: ")
                    print("")
                    contador = 0
                    contador_rob = 0
                    while nodo_tem_tienen != None:
                        contador += 1
                        print("\t -----> "+str(contador)+" "+nodo_tem_tienen.objeto_ciudad.nombre)
                        
                        nodo_tem_tienen = nodo_tem_tienen.siguiente
                        print("")
                    print("Y ESTOS SON LOS ROBOTS DISPONIBLES: ")
                    while nodo_tem_rob != None:
                        contador_rob += 1
                        print("\t -----> "+str(contador_rob)+" "+nodo_tem_rob.objeto_robot.nombre+""+nodo_tem_rob.objeto_robot.capacidad)  
                        nodo_tem_rob = nodo_tem_rob.siguiente
                    print("")
                    if contador == 1:
                                print("PUESTO QUE SOLO HAY UNA CIUDAD LA MISION SE LLEVARA ACABO EN ESTA")
                                nodo_tem_tienen = lista_tienen_rescate.head
                                ciudad_elegida = nodo_tem_tienen.objeto_ciudad
                                lista_celdas = lista_rescates(tipo_celda, nodo_tem_tienen.objeto_ciudad)
                                print(nodo_tem_tienen.objeto_ciudad.nombre)
                                nodo_celda = Estructuras_celda.Nodo('')
                                nodo_celda = lista_celdas.head
                                contador_celdas = 0
                                while nodo_celda != None:
                                    contador_celdas += 1
                                    print(str(contador_celdas)+". --->"+"FILA: "+str(nodo_celda.objeto_celda.fila)+", COLUMNA: "+str(nodo_celda.objeto_celda.columna))
                                    nodo_celda = nodo_celda.siguiente
                                if contador_celdas == 1:
                                    print("SOLO HAY UNA UNIDAD A RESCATAR ASI QUE LA MISION SE LLEVARA A CABO EN ESTA")
                                    nodo_celda = lista_celdas.head
                                    celda_rescatar  = nodo_celda.objeto_celda
                                    

                                else: 
                                    opcion_celda = int(input("ELIJA LA UNIDAD QUE DESEA RESCATAR: "))
                                    contador_celda_ele = 0
                                    nodo_celda = lista_celdas.head
                                    while nodo_celda != None:
                                        contador_celda_ele += 1
                                        if contador_celda_ele == opcion_celda:
                                            celda_rescatar = nodo_celda.objeto_celda
                                        nodo_celda = nodo_celda.siguiente
                        
                    else:
                        opcion_ciudad = int(input("ELIJA EL NUMERO DE CIUDAD DONDE DESEA REALIZAR LA MISION: "))
                        contador_ciu_ele = 0
                        nodo_tem_tienen = lista_tienen_rescate.head
                        while nodo_tem_tienen != None:
                            contador_ciu_ele += 1
                            if contador_ciu_ele == opcion_ciudad:
                                ciudad_elegida = nodo_tem_tienen.objeto_ciudad
                                lista_celdas = lista_rescates(tipo_celda, nodo_tem_tienen.objeto_ciudad)
                                print(nodo_tem_tienen.objeto_ciudad.nombre)
                                print("")
                                nodo_celda = Estructuras_celda.Nodo('')
                                nodo_celda = lista_celdas.head
                                contador_celdas = 0
                                while nodo_celda != None:
                                    contador_celdas += 1
                                    print(str(contador_celdas)+". ---> "+"FILA: "+str(nodo_celda.objeto_celda.fila)+", COLUMNA: "+str(nodo_celda.objeto_celda.columna))
                                    nodo_celda = nodo_celda.siguiente
                                if contador_celdas == 1:
                                    print("")
                                    print("SOLO HAY UNA UNIDAD A RESCATAR ASI QUE LA MISION SE LLEVARA A CABO EN ESTA")
                                    nodo_celda = lista_celdas.head
                                    celda_rescatar  = nodo_celda.objeto_celda

                                else: 
                                    print("")
                                    opcion_celda = int(input("ELIJA LA UNIDAD QUE DESEA RESCATAR: "))
                                    contador_celda_ele = 0
                                    nodo_celda = lista_celdas.head
                                    while nodo_celda != None:
                                        contador_celda_ele += 1
                                        if contador_celda_ele == opcion_celda:
                                            celda_rescatar = nodo_celda.objeto_celda
                                        nodo_celda = nodo_celda.siguiente

                                #lista_celdas.imprimirLista()
                            
                            nodo_tem_tienen = nodo_tem_tienen.siguiente
                            

                    #print(ciudad_elegida.nombre)
                    #celda_rescatar.mostrar_celda()

                    if contador_rob == 1:
                        print("SOLO HAY UN ROBOT ENTONCES ESTE EJECUTARA LA MISION")
                        nodo_tem_rob = lista_hay_robot.head
                        robot_elegido = nodo_tem_rob.objeto_robot
                    else:
                        opcion_rob_ele = int(input("ELIJA EL ROBOT QUE LLEVARA A CABO LA MISION: "))
                        contador_rob_ele = 0
                        nodo_tem_rob = lista_hay_robot.head
                        while nodo_tem_rob != None:
                            contador_rob_ele += 1
                            if contador_rob_ele == opcion_rob_ele:
                                robot_elegido = nodo_tem_rob.objeto_robot
                            nodo_tem_rob = nodo_tem_rob.siguiente
                        
                    print("")
                    #robot_elegido.mostrar_robot()
                    arreglo_ciudad_celda_rob[0] = ciudad_elegida
                    arreglo_ciudad_celda_rob[1] = celda_rescatar
                    arreglo_ciudad_celda_rob[2] = robot_elegido
                    return arreglo_ciudad_celda_rob
                    
  
                else:
                    print("NO SE PUEDE REALIZAR ESTA MISION PORQUE NO HAY LOS RECURSOS DISPONIBLES")
                    
                    return arreglo_ciudad_celda_rob

                


def lista_rescates (tipo, ciudad):
    lista_filas = ciudad.filas
    nodofila = Estructuras_filas.Nodo("")
    nodofila = lista_filas.head
    lista_celdas = Estructuras_celda.ListaDoble_celda()
    
    while nodofila != None:
        caracteres = nodofila.objeto_fila.lista
        contador_col = 0
        for caracter in caracteres:
            
            if caracter == tipo:
                nueva_celda = Celda(nodofila.objeto_fila.numero, contador_col, caracter)
                lista_celdas.añadirNodoPrincipio(nueva_celda)
            contador_col +=1
        
        nodofila = nodofila.siguiente
    
    return lista_celdas

def buscar_robot(tipo, lista):
                nodo_temp = Estructuras_robot.Nodo('')
                nodo_temp = lista.head
                lista_robots_enc = Estructuras_robot.ListaDoble_robot()
                
                while nodo_temp != None:
                    si_hay = False
                    
                    if nodo_temp.objeto_robot.tipo == tipo:
                        si_hay = True
                        
                    if si_hay == False: 
                        pass
                    else: 
                        lista_robots_enc.añadirNodoPrincipio(nodo_temp.objeto_robot)
                    nodo_temp = nodo_temp.siguiente
                
                return lista_robots_enc

def buscar_ciudades (caracter_busc, lista):
                nodo_temp = Esstructura_ciudades.Nodo('')
                nodo_temp = lista.head
                lista_ciudades_enc = Esstructura_ciudades.ListaDoble()
                
                while nodo_temp != None:
                    cadena_caracteres = ""
                    lista_filas_nodo_temp = nodo_temp.objeto_ciudad.filas
                    nodo_fila = Estructuras_filas.Nodo("")
                    nodo_fila = lista_filas_nodo_temp.head
                    while nodo_fila != None:
                        cadena_caracteres += nodo_fila.objeto_fila.lista 
                        nodo_fila = nodo_fila.siguiente
                    si_hay = False
                    for caracter in cadena_caracteres:
                        if caracter == caracter_busc:
                            si_hay = True
                            break
                    if si_hay == False: 
                        pass
                    else: 
                        lista_ciudades_enc.añadirNodoPrincipio(nodo_temp.objeto_ciudad)
                    nodo_temp = nodo_temp.siguiente
                
                return lista_ciudades_enc

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  

    