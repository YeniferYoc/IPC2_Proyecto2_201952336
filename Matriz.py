from Nodo_Cabecera import Nodo_Cabecera
from Lista_Cabecera import Lista_Cabecera
import os
import webbrowser


class Nodo_Celda(): 
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.coordenadaX = x  
        self.coordenadaY = y 
        self.arriba = None
        self.abajo = None
        self.derecha = None  
        self.izquierda = None  # self.anterior

    def setArriba(self, arriba):
        self.arriba = arriba
    

    def getArriba(self):
        return self.arriba
    

    def setAbajo(self, abajo):
        self.abajo = abajo
    

    def getAbajo(self):
        return self.abajo


    def setDerecha(self, derecha):
        self.derecha = derecha
    

    def getDerecha(self):
        return self.derecha
    

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda
    

    def getIzquierda(self):
        return self.izquierda


class Matriz():
    def __init__(self):
        self.capa = 0
        self.filas = Lista_Cabecera('fila')
        self.columnas = Lista_Cabecera('columna')

    # (filas = x, columnas = y)
    def insertar(self, pos_x, pos_y, caracter):
        nueva_celda = Nodo_Celda(pos_x, pos_y, caracter) # se crea nodo celda a insertar
        # --- lo prinero sera buscar si ya existen los cabeceras en la matriz
        nodo_X = self.filas.getCabecera(pos_x)
        nodo_Y = self.columnas.getCabecera(pos_y)

        if nodo_X == None: # --- comprobamos que el cabecera fila pos_x exista
             # --- si nodo_X es nulo, quiere decir que no existe cabecera fila pos_x
            nodo_X = Nodo_Cabecera(pos_x)
            self.filas.insertar_nodoCabecera(nodo_X)

        if nodo_Y == None: # --- comprobamos que el cabecera columna pos_y exista
            # --- si nodo_Y es nulo, quiere decir que no existe  columna pos_y
            nodo_Y = Nodo_Cabecera(pos_y)
            self.columnas.insertar_nodoCabecera(nodo_Y)

        # ----- INSERTAR NUEVA_CELDA EN FILA
        if nodo_X.getAcceso() == None: # -- comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_X.setAcceso(nueva_celda)
        else: # -- si esta apuntando, validamos si la posicion de la columna del nueva_celda nodoInterno es menor a la posicion de la columna del acceso 
            if nueva_celda.coordenadaY < nodo_X.getAcceso().coordenadaY: # F1 --->  NI 1,1     NI 1,3      
                nueva_celda.setDerecha(nodo_X.getAcceso())        
                nodo_X.getAcceso().setIzquierda(nueva_celda)
                nodo_X.setAcceso(nueva_celda)
            else:
                #de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el nueva_celda nodoInterno
                tmp : Nodo_Celda = nodo_X.getAcceso() 
                while tmp != None:                      
                    if nueva_celda.coordenadaY < tmp.coordenadaY:
                        nueva_celda.setDerecha(tmp)
                        nueva_celda.setIzquierda(tmp.getIzquierda())
                        tmp.getIzquierda().setDerecha(nueva_celda)
                        tmp.setIzquierda(nueva_celda)
                        break
                    elif nueva_celda.coordenadaX == tmp.coordenadaX and nueva_celda.coordenadaY == tmp.coordenadaY: #validamos que no haya repetidas
                        break
                    else:
                        if tmp.getDerecha() == None:
                            tmp.setDerecha(nueva_celda)
                            nueva_celda.setIzquierda(tmp)
                            break
                        else:
                            tmp = tmp.getDerecha() 
                           
        # ----- INSERTAR NUEVA_CELDA EN COLUMNA
        if nodo_Y.getAcceso() == None:  # -- comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_Y.setAcceso(nueva_celda)
        else: # -- si esta apuntando, validamos si la posicion de la fila del nueva_celda nodoCelda es menor a la posicion de la fila del acceso 
            if nueva_celda.coordenadaX < nodo_Y.getAcceso().coordenadaX:
                nueva_celda.setAbajo(nodo_Y.getAcceso())
                nodo_Y.getAcceso().setArriba(nueva_celda)
                nodo_Y.setAcceso(nueva_celda)
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el nueva_celda
                tmp2 : Nodo_Celda = nodo_Y.getAcceso()
                while tmp2 != None:
                    if nueva_celda.coordenadaX < tmp2.coordenadaX:
                        nueva_celda.setAbajo(tmp2)
                        nueva_celda.setArriba(tmp2.getArriba())
                        tmp2.getArriba().setAbajo(nueva_celda)
                        tmp2.setArriba(nueva_celda)
                        break
                    elif nueva_celda.coordenadaX == tmp2.coordenadaX and nueva_celda.coordenadaY == tmp2.coordenadaY: #validamos que no haya repetidas
                        break
                    else:
                        if tmp2.getAbajo() == None:
                            tmp2.setAbajo(nueva_celda)
                            nueva_celda.setArriba(tmp2)
                            break
                        else:
                            tmp2 = tmp2.getAbajo()
        ##------ Fin de insercion

    def recorridoPorFila(self, fila):
        inicio : Nodo_Cabecera = self.filas.getCabecera(fila)
        if inicio == None:
            print('Esa coordenada de filas no existe')
            return None
            
        tmp : Nodo_Celda = inicio.getAcceso()
        #tmp = self.filas.getCabecera(fila).getAcceso()
        while tmp != None:
            print(tmp.caracter)
            tmp = tmp.getDerecha()

    
    def recorridoPorColumna(self, columna):
        inicio : Nodo_Cabecera = self.columnas.getCabecera(columna)
        if inicio == None:
            print('Esa coordenada de columna no existe')
            return None

        tmp : Nodo_Celda = inicio.getAcceso()
        #tmp = self.filas.getCabecera(fila).getAcceso()
        while tmp != None:
            print(tmp.caracter)
            tmp = tmp.getAbajo()


    def ubicarCoordenada(self, fila, columna):
        try:
            tmp : Nodo_Celda = self.filas.getCabecera(fila).getAcceso()
            while tmp != None:
                if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                    return tmp
                tmp = tmp.getDerecha()
            return None
        except:
            print('Coordenada no encontrada')
            return None
    
    def ubicaryCambiar(self, fila, columna, caracter_nuevo):
        try:
            tmp : Nodo_Celda = self.filas.getCabecera(fila).getAcceso()
            while tmp != None:
                if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                    tmp.caracter = caracter_nuevo
                tmp = tmp.getDerecha()
            return None
        except:
            print('Coordenada no encontrada')
            return None

    

    '''def MisionCivil(self, fila_e, columna_e, fila_fin, columna_fin):
        
        tmp : Nodo_Celda = self.filas.getCabecera(fila).getAcceso()
        while tmp != None:
            if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                return tmp
            tmp = tmp.getDerecha()
        return None'''
        
