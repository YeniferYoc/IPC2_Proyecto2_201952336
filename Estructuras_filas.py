class Nodo:
    def __init__(self, objeto_fila):
        self.objeto_fila = objeto_fila
        self.siguiente = None
        self.anterior = None

class ListaDoble_fila:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_fila):
        nuevoNodo = Nodo(obj_fila)

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
        print("---------------------------------- FILAS ------------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("FILA:"+str(contador)+" -> "+nodoTemporal.objeto_fila.numero+" CADENA DE FILA: "+nodoTemporal.objeto_fila.lista)
            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

