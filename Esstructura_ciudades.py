class Nodo:
    def __init__(self, objeto_ciudad):
        self.objeto_ciudad = objeto_ciudad
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_ciudad):
        nuevoNodo = Nodo(obj_ciudad)

        #Validamos si la lista esta vacia
        if self.head == None:
           # print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo
        
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            #print("*** ORDENANDO***")
            nodoTemporal = Nodo("")

            nodoTemporal = self.head
            if nodoTemporal.objeto_ciudad.nombre > nuevoNodo.objeto_ciudad.nombre:
                self.head.anterior = nuevoNodo
                nuevoNodo.siguiente = self.head
                self.head = nuevoNodo
            else:
                #print("Insertando nodo al final")
                self.end.siguiente = nuevoNodo
                nuevoNodo.anterior = self.end
                self.end = nuevoNodo


    def imprimirLista(self):
        
        print("-------------------------------------- CIUDADES -------------------------------------- ")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print(" -> "+"NOMBRE: "+nodoTemporal.objeto_ciudad.nombre+" FILAS:"+str(nodoTemporal.objeto_ciudad.cant_filas)+" COLUMNAS: "+str(nodoTemporal.objeto_ciudad.cant_columnas))
            print("")
            nodoTemporal.objeto_ciudad.filas.imprimirLista()

            print("")

            nodoTemporal.objeto_ciudad.unidades_militares.imprimirLista()
            print("--------------------------------------------------------------------------------")

            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

    def imprimir_nombre_ciudades(lista):
        nodoTemporal = Nodo("")

        nodoTemporal = lista.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print(str(contador)+" -> "+"NOMBRE: "+nodoTemporal.objeto_piso.nombre)

            nodoTemporal = nodoTemporal.siguiente

        print("")
        print("")