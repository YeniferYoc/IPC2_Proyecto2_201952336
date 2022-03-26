class Nodo:
    def __init__(self, objeto_celda):
        self.objeto_celda = objeto_celda
        self.siguiente = None
        self.anterior = None

class ListaDoble_celda:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_celda):
        nuevoNodo = Nodo(obj_celda)

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
        print("---------------------------------- CELDAS ------------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
       
        while nodoTemporal != None:
            
            print("FILA: "+str(nodoTemporal.objeto_celda.fila)+" COLUMNA:  "+str(nodoTemporal.objeto_celda.columna)+" TIPO: "+nodoTemporal.objeto_celda.tipo)
            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

