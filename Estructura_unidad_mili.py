class Nodo:
    def __init__(self, objeto_unidad):
        self.objeto_unidad = objeto_unidad
        self.siguiente = None
        self.anterior = None

class ListaDoble_unidad:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_unidad):
        nuevoNodo = Nodo(obj_unidad)

        #Validamos si la lista esta vacia
        if self.head == None:
           # print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo
        
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            #print("*** ORDENANDO***")
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo
        
    def imprimirLista(self):
        print("--------------------------------------------------------------------------------")
        print("---------------------------------- UNIDADES MILITARES ------------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("FILA:"+str(contador)+" -> "+str(nodoTemporal.objeto_unidad.fila)+" COLUMNA: "+str(nodoTemporal.objeto_unidad.columna)+" CAPACIDAD: "+str(nodoTemporal.objeto_unidad.capacidad))
            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

