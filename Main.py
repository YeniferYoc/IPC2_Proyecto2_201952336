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
from Matriz import *

lista_ciudades = Esstructura_ciudades.ListaDoble()
lista_robots = Estructuras_robot.ListaDoble_robot()
ciudad_elegida = None
celda_rescatar  = None
civil = False
recurso = False
robot_elegido = None
matriz = Matriz()



def menu(): 
    salir = False
  
    while salir != True:    
        #AQUI ESTA EL MENU PRINCIPAL    
        print("")
        print("--------------------------------------------------------------------")
        print("1. CARGAR XML")
        print("2. ELEGIR MISION")
        print("3. VER GRAFICA DE LA CIUDAD")
        print("4. EJECUTAR MISION")
        print("5. SALIR")
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
                        cant_filas = int(node.getAttribute("filas"))
                        #print(cant_filas)
                        cant_columnas = int(node.getAttribute("columnas"))
                        #print(cant_columnas)
                    
                    filas = ciudad.getElementsByTagName('fila')
                    lista_filas = Estructuras_filas.ListaDoble_fila()
                    for fila in filas:
                        numero = int(fila.attributes['numero'].value) 
                        lista_letras = fila.childNodes[0].data
                        lista_letras = lista_letras.replace('"','')
                        fila_nueva = Fila(numero, lista_letras)
                        lista_filas.añadirNodoPrincipio(fila_nueva)

                    unidadMilitares = ciudad.getElementsByTagName('unidadMilitar')
                    lista_unidades = Estructura_unidad_mili.ListaDoble_unidad()
                    for unidad in unidadMilitares:
                        fila_u = int(unidad.attributes['fila'].value)
                        columna_u = int(unidad.attributes['columna'].value)
                        capacidad_u = int(unidad.childNodes[0].data)
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
                                nodo_temporal.objeto_ciudad.cant_filas = int(node.getAttribute("filas"))
                                nodo_temporal.objeto_ciudad.cant_columnas = int(node.getAttribute("columnas"))
                            #SOBREESCRIBIMOS LA LISTA DE LAS FILAS
                            filas2 = ciudad.getElementsByTagName('fila')
                            lista_filas_sobre = Estructuras_filas.ListaDoble_fila()
                            for fila in filas2:
                                numero_sobre = int(fila.attributes['numero'].value) 
                                lista_letras_sobre = fila.childNodes[0].data
                                lista_letras_sobre = lista_letras_sobre.replace('"','')
                                fila_nueva_sobre = Fila(numero_sobre, lista_letras_sobre)
                                lista_filas_sobre.añadirNodoPrincipio(fila_nueva_sobre)
                            nodo_temporal.objeto_ciudad.filas = lista_filas_sobre
                            repetido = True
                            
                            unidadMilitares2 = ciudad.getElementsByTagName('unidadMilitar')
                            lista_unidades_sobres = Estructura_unidad_mili.ListaDoble_unidad()
                            for unidad in unidadMilitares2:
                                fila_u2 = int(unidad.attributes['fila'].value)
                                columna_u2 = int(unidad.attributes['columna'].value)
                                capacidad_u2 = int(unidad.childNodes[0].data)
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
                                cant_filas = int(node.getAttribute("filas"))
                                #print(cant_filas)
                                cant_columnas = int(node.getAttribute("columnas"))
                                #print(cant_columnas)
                            
                            filas = ciudad.getElementsByTagName('fila')
                            lista_filas = Estructuras_filas.ListaDoble_fila()
                            for fila in filas:
                                numero = int(fila.attributes['numero'].value) 
                                lista_letras = fila.childNodes[0].data
                                lista_letras = lista_letras.replace('"','')
                                fila_nueva = Fila(numero, lista_letras)
                                lista_filas.añadirNodoPrincipio(fila_nueva)
                            
                            unidadMilitares = ciudad.getElementsByTagName('unidadMilitar')
                            lista_unidades = Estructura_unidad_mili.ListaDoble_unidad()
                            for unidad in unidadMilitares:
                                fila_u = int(unidad.attributes['fila'].value)
                                columna_u = int(unidad.attributes['columna'].value)
                                capacidad_u = int(unidad.childNodes[0].data)
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
                ciudad_elegida = arreglo[0]
                celda_rescatar = arreglo[1]
                robot_elegido = arreglo[2]
                civil = True
                print("-----------------------------> CIUDAD: \t"+ciudad_elegida.nombre)
                print("-----------------------------> CELDA A RESCATAR: ")
                celda_rescatar.mostrar_celda()
                print("-----------------------------> ROBOT ENCARGADO: ")
                robot_elegido.mostrar_robot()

            if opcion_mision == 2:############################### AQUI VA LA MISION 2
                arreglo2 = Seleccionar_ciudad_celda('R','ChapinFighter', lista_ciudades, lista_robots )
                print("")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° RESUMEN DE MISION °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                ciudad_elegida = arreglo2[0]
                celda_rescatar = arreglo2[1]
                robot_elegido = arreglo2[2]
                civil = True
                print("------------> CIUDAD: \t"+ciudad_elegida.nombre)
                print("------------> CELDA A RESCATAR: ")
                celda_rescatar.mostrar_celda()
                print("------------> ROBOT ENCARGADO: ")
                robot_elegido.mostrar_robot()
            
            ################################### LLENANDO MATRIZ #######################################
            lista_elegida = ciudad_elegida.filas
            nodo_fila = Estructuras_filas.Nodo("")
            nodo_fila = lista_elegida.head
            
            print("LLENANDO MATRIZ")
            filaa = 1
            while nodo_fila != None:
                caracteres = nodo_fila.objeto_fila.lista
                contador_col = 1
                for caracter in caracteres:
                    print(str(filaa)+","+str(contador_col))
                    matriz.insertar(filaa, contador_col, caracter)
                    contador_col +=1
                filaa += 1

                nodo_fila = nodo_fila.siguiente
            
            ################################### CAMBIAR MILITAR ###################################
            nodo_mili = Estructura_unidad_mili.Nodo('')
            nodo_mili = ciudad_elegida.unidades_militares.head

            while nodo_mili != None:
                fila_mili = nodo_mili.objeto_unidad.fila
                col_mili = nodo_mili.objeto_unidad.columna
                capacidad_mili = nodo_mili.objeto_unidad.capacidad
                matriz.ubicaryCambiar(fila_mili, col_mili, capacidad_mili)
            
                nodo_mili = nodo_mili.siguiente
 
        if(opcion == 3):
            #################### PASAR MATRIZ A LISTA PARA GRAFICAR ###################
            print("GRAFICANDO")
            lista_graf = Estructuras_celda.ListaDoble_celda()
            nodo = Estructuras_celda.Nodo('')
            nodo = lista_graf.head
            fil = int(ciudad_elegida.cant_filas)
            col = int(ciudad_elegida.cant_columnas)
            for i in range(1,fil+1,1):
                for j in range(1,col+1,1):
                    
                    nodo = matriz.ubicarCoordenada(i,j)
                    print(nodo.caracter)
                    celda = Celda(i, j,nodo.caracter)
                    lista_graf.añadirNodoPrincipio(celda)
            lista_graf.imprimirLista()
            Generar_graphviz(lista_graf,ciudad_elegida)

        if(opcion == 4):
            mat_aux = matriz
            matriz_nueva = Ubicar_entrada(mat_aux, ciudad_elegida, celda_rescatar)
            '''print("coordenadas entrada")
            print(entrada[0])
            print(entrada[1])'''
            #################### PASAR MATRIZ A LISTA PARA GRAFICAR ###################
            print("GRAFICANDO")
            lista_graf = Estructuras_celda.ListaDoble_celda()
            nodo = Estructuras_celda.Nodo('')
            nodo = lista_graf.head
            fil = int(ciudad_elegida.cant_filas)
            col = int(ciudad_elegida.cant_columnas)
            for i in range(1,fil+1,1):
                for j in range(1,col+1,1):
                    
                    nodo = matriz_nueva.ubicarCoordenada(i,j)
                    #print(nodo.caracter)
                    celda = Celda(i, j,nodo.caracter)
                    lista_graf.añadirNodoPrincipio(celda)
            lista_graf.imprimirLista()
            Generar_graphviz(lista_graf,ciudad_elegida)
            
            if civil == True:
                pass
            if recurso == True:
                pass
            
        if(opcion == 5):
            print("ADIOOOOS!! :)")
            salir = True
                  
def Ubicar_entrada(matriz_u, ciudad, celda_civil):
        '''tmp = Nodo_Celda(1,1,'')
        tmp = matriz.capa'''
        coordenada = [0,0]
        filas = int(ciudad.cant_filas)
        x_fin = celda_civil.fila
        y_fin = celda_civil.columna
 
        for i in range(1,filas):   
            tmp : Nodo_Celda = matriz_u.filas.getCabecera(i).getAcceso()
            while tmp != None:
                if tmp.caracter == 'E': #SI ENCUENTRA UNA ENTRADA ENTONCES A PARTIR DE AQUI DEBE TRAZAR UN CAMINO
                    #PRIMERO DEBEMOS SABER DONDE ESTA LA UNIDAD CIVIL SI A LA DERECHA O IQUIERDA
                        fila = tmp.coordenadaX
                        col = tmp.coordenadaY
                        completada = False
                    
                        #if col > y_fin and fila == x_fin: le puse un tab a la derecha
                        
                        #VEREMOS SI SE PUEDE MOVER A LA IZQUIERDA
                        temp_cambia : Nodo_Celda = matriz_u.filas.getCabecera(i).getAcceso()
                        while temp_cambia != None: #EL TEMPORAL BUSCA LA POSICION DE LA ENTRADA
                            if temp_cambia.coordenadaX == fila and temp_cambia.coordenadaY == col:
                                print("encontre entrada")
                                #AHORA QUE LO ENCONTRO DEBE CAMBIAR EL CAMINO
                                temp_cambia.caracter = '#'
                                salir_a = False
                                while salir_a != True:#HASTA QUE LLEGE
                                    
                                    print(temp_cambia.coordenadaY)
                                    print(y_fin)
                                    print(temp_cambia.coordenadaX)
                                    print(x_fin)
                                    ban_iz = False
                                    ban_der = False
                                    ban_arr = False
                                    ban_abb = False 

                                    #VALIDACION DE NULOS 
                                    '''nulo_iz = False
                                    nulo_der = False
                                    nulo_arr = False
                                    nulo_abb = False
                                    if temp_cambia.izquierda == None:
                                        nulo_iz = True
                                    if temp_cambia.derecha == None:
                                        nulo_der = True
                                    if temp_cambia.arriba == None:
                                        nulo_arr = True
                                    if temp_cambia.abajo == None:
                                        nulo_abb = True'''
                                    

                                    #SI PUEDE AVANZAR A LA IZQUIERDA
                                    if temp_cambia.izquierda != None:
                                        if temp_cambia.izquierda.caracter == 'E' or temp_cambia.izquierda.caracter == ' ' or temp_cambia.izquierda.caracter == 'C':
                                            print("SI PUEDE TRANSITAR iz")
                                            if temp_cambia.coordenadaY == y_fin and temp_cambia.coordenadaX == x_fin:
                                                print("MISION COMPLETA")
                                                salir_a = True
                                                break
                                            else: 
                                                temp_cambia.izquierda.caracter = '#'
                                                temp_cambia = temp_cambia.izquierda
                                                ban_iz = True
                                                continue
                                                
                                        else:#EVALUAMOS SI SE PUEDE REGRESAR SIN PASAR POR EL NUMERAL
                                            nodo_num : Nodo_Celda = matriz_u.filas.getCabecera(temp_cambia.coordenadaX).getAcceso()
                                            while nodo_num != None: #EL TEMPORAL BUSCA LA POSICION DE LA ENTRADA
                                                if temp_cambia.coordenadaX == nodo_num.coordenadaX and nodo_num.coordenadaX == temp_cambia.coordenadaX:
                                                    #LO ENCONTRO
                                                    while nodo_num.caracter == '#':
                                                        nodo_num = nodo_num.derecha
                                                    if nodo_num != None:
                                                        if nodo_num.caracter == 'E' or nodo_num.caracter == ' ' or nodo_num.caracter == 'C':
                                                            temp_cambia.coordenadaX = nodo_num.coordenadaX
                                                            temp_cambia.coordenadaY = nodo_num.coordenadaY
                                                            temp_cambia.caracter = '#'
                                                            ban_iz = True
                                                            break
                                                        else: 
                                                            print("aquie no")
                                                            print(str(temp_cambia.coordenadaX)+" FILA MIO iz")
                                                            print(str(temp_cambia.coordenadaY)+" COLUMNA MIO iz")
                                                            break
                                            
                                                nodo_num = nodo_num.derecha

                                    #este rogrmama 
                                    #SI PUEDE AVANZAR A LA DERECHA
                                    if temp_cambia.derecha != None:
                                        if temp_cambia.derecha.caracter == 'E' or temp_cambia.derecha.caracter == ' ' or temp_cambia.derecha.caracter == 'C':
                                            print("SI PUEDE TRANSITAR dwer")
                                            if temp_cambia.coordenadaY == y_fin and temp_cambia.coordenadaX == x_fin:
                                                print("MISION COMPLETA")
                                                salir_a = True
                                                break 
                                            else:
                                                temp_cambia.derecha.caracter = '#'
                                                temp_cambia = temp_cambia.derecha
                                                ban_der = True
                                                continue
                                                
                                        
                                        else:#EVALUAMOS SI SE PUEDE REGRESAR SIN PASAR POR EL NUMERAL
                                            auxx= temp_cambia.coordenadaX
                                            auxy = temp_cambia.coordenadaY
                                            nodo_num : Nodo_Celda = matriz_u.filas.getCabecera(temp_cambia.coordenadaX).getAcceso()
                                            while nodo_num != None: #EL TEMPORAL BUSCA LA POSICION DE LA ENTRADA
                                                if temp_cambia.coordenadaX == nodo_num.coordenadaX and nodo_num.coordenadaY == temp_cambia.coordenadaY:
                                                    #LO ENCONTRO
                                                    while nodo_num.caracter == '#':
                                                        nodo_num = nodo_num.izquierda
                                                    print(nodo_num.caracter+" fila "+str(nodo_num.coordenadaX)+" columna "+str(nodo_num.coordenadaY))
                                                    if nodo_num != None:
                                                        if nodo_num.caracter == 'E' or nodo_num.caracter == ' ' or nodo_num.caracter == 'C':
                                                            temp_cambia.coordenadaX = nodo_num.coordenadaX
                                                            temp_cambia.coordenadaY = nodo_num.coordenadaY
                                                            temp_cambia.caracter = '#'
                                                            ban_der = True
                                                            break
                                                        else: 
                                                            print("aquie no")
                                                            temp_cambia.coordenadaX = auxx
                                                            temp_cambia.coordenadaY = auxy
                                                            print(str(temp_cambia.coordenadaX)+" FILA MIO")
                                                            print(str(temp_cambia.coordenadaY)+" COLUMNA MIO")
                                                            break
                                            
                                                nodo_num = nodo_num.derecha

                                    else: 
                                        pass
                                    #SI PUEDE AVANZAR HACIA ARRIBA
                                    if temp_cambia.arriba != None:
                                        if temp_cambia.arriba.caracter == 'E' or temp_cambia.arriba.caracter == ' ' or temp_cambia.arriba.caracter == 'C' :
                                            print("SI PUEDE TRANSITAR arr")
                                            if temp_cambia.coordenadaY == y_fin and temp_cambia.coordenadaX == x_fin:
                                                print(str(temp_cambia.coordenadaX)+","+str(temp_cambia.coordenadaY))
                                                print("MISION COMPLETA")
                                                salir_a = True
                                                break
                                            else: 
                                                temp_cambia.arriba.caracter = '#'
                                                temp_cambia = temp_cambia.arriba
                                                ban_arr = True
                                                continue
                                                
                                    else:
                                        pass
                                    #SI PUEDE AVANZAR HACIA ABAJO
                                    if temp_cambia.abajo != None:
                                        if temp_cambia.abajo.caracter == 'E' or temp_cambia.abajo.caracter == ' ' or temp_cambia.abajo.caracter == 'C' :
                                            print("SI PUEDE TRANSITAR abb")
                                            if temp_cambia.coordenadaY == y_fin and temp_cambia.coordenadaX == x_fin:
                                                print("MISION COMPLETA")
                                                salir_a = True
                                                break
                                            else: 
                                                temp_cambia.abajo.caracter = '#'
                                                temp_cambia = temp_cambia.abajo
                                                ban_abb = True
                                                continue
                                                
                                    else:
                                        pass
                                    
                                    
                                    if ban_der == True or ban_iz == True or ban_arr == True or ban_abb == True:
                                        ban_iz = False
                                        ban_der = False
                                        ban_arr = False
                                        ban_abb = False
                                    else:
                                        print("no se puede transitar")
                                        salir_a = True
                                    #temp_cambia = temsp_cambia.izquierda 
                                break   
                            temp_cambia = temp_cambia.getDerecha()
                        
                        if temp_cambia.coordenadaY == y_fin:
                            print("MISION COMPLETADA")
                            salir_a = True

                            break
                        else:
                            print("MISION IMPOSIBLE")

                    
                tmp = tmp.derecha
        
        return matriz_u


'''elif col < y_fin and fila == x_fin:
                        print("DEBO MOVERME A LA IZQUIERDA")
                    elif fila > x_fin and col == y_fin:
                        print("DEBO MOVERME HACIA ARRIBA")
                    elif fila < x_fin and col == y_fin:
                        print("DEBO MOVERME HACIA ABAJO")aqui termina el cambio, son dos bloques diferentes


                    coordenada[0] = tmp.coordenadaX
                    coordenada[1] = tmp.coordenadaY'''

'''def Ubicar_entrada(matriz_u, ciudad, celda_civil):
        
        coordenada = [0,0]
        filas = int(ciudad.cant_filas)
        x_fin = celda_civil.fila
        y_fin = celda_civil.columna

        
        for i in range(1,filas):
            
            tmp : Nodo_Celda = matriz_u.filas.getCabecera(i).getAcceso()
            while tmp != None:
                if tmp.caracter == 'E':
                    coordenada[0] = tmp.coordenadaX
                    coordenada[1] = tmp.coordenadaY
                tmp = tmp.derecha
        
        return coordenada'''

def Generar_graphviz(lista, ciudad):    
    filas = int(ciudad.cant_filas)
    columnas = int(ciudad.cant_columnas)

    mi_archivo= open('matriz.dot','w')
    mi_archivo.write("digraph L{")
    mi_archivo.write("node[shape = box fillcolor = \"#FFEDBB\" style  = filled]")
    mi_archivo.write("subgraph cluster_p{")
    mi_archivo.write("label= \"MATRIZ\"")
    mi_archivo.write("bgcolor = \"#398D9C\"")
    mi_archivo.write("edge [dir = \"both\"]")
    celda="celda"
    contador = 1 
    mensaje =''
    print("*** Imprimiendo Celdas ***")
    nodoTemporal = Estructuras_celda.Nodo("")

    nodoTemporal = lista.head
    
 
    for i in range(filas):
        for j in range(columnas):
            mensaje =str(celda+str(contador))
            color_celda = str(nodoTemporal.objeto_celda.tipo)
            if color_celda.upper() == ' ':
                color_celda = 'white'
            elif color_celda.upper() == '*':
                color_celda = 'black'
            elif color_celda.upper() == '#':
                color_celda = 'orange'
            elif color_celda.upper() == 'E':
                color_celda = 'green'
            elif color_celda.upper() == 'C':
                color_celda = 'blue'
            elif color_celda.upper() == 'R':
                color_celda = 'gray'
            elif color_celda.isdigit():
                color_celda = 'red'
            else:
                color_celda = 'yellow'   
            nodoTemporal = nodoTemporal.siguiente
            mi_archivo.write(mensaje+"[label= \""+str(contador)+"\", fillcolor ="+color_celda+", group = 2 ];")
            contador += 1 

    total_celdas = filas* columnas
    
    mensaje = ''
    for j in range(1, total_celdas-filas+1, columnas):
        contador2 = j
        for i in range(1,columnas,1):
            mensaje =str(celda+str(contador2))
            sig_fila = str(celda+str(contador2+1))
            mi_archivo.write(mensaje+"->"+sig_fila+";")
            contador2+=1
    
    for j in range(1, total_celdas-filas+1, columnas):
        contador2 = j
        mi_archivo.write("{rank = same;")
        for i in range(1,columnas+1,1):
            mensaje =str(celda+str(contador2))
            mi_archivo.write(mensaje+";")
            contador2+=1

        mi_archivo.write("}")

    
    
    for j in range(1, columnas+1, 1):
        for i in range(j,total_celdas-columnas+1,columnas):
            mensaje =str(celda+str(i))
            sig_fila = str(celda+str(i+columnas))
            mi_archivo.write(mensaje+"->"+sig_fila+";")
    

    mi_archivo.write("}")
    mi_archivo.write("}")

    mi_archivo.close()

    system('dot -Tpng matriz.dot -o matriz.png')
    system('cd./matriz.png')
    startfile('matriz.png')                
                
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
        contador_col = 1
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
  

    