class Nodo:
    def __init__(self, objeto_robot):
        self.objeto_robot = objeto_robot
        self.siguiente = None
        self.anterior = None

class ListaDoble_robot:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_robot):
        nuevoNodo = Nodo(obj_robot)

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
        print("---------------------------------- ROBOTS ------------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("ROBOT:"+str(contador)+" -> "+nodoTemporal.objeto_robot.nombre+" TIPO: "+nodoTemporal.objeto_robot.tipo+" CAPACIDAD: "+nodoTemporal.objeto_robot.capacidad)
            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

