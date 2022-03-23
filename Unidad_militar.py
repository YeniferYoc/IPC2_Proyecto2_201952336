class Unidad_militar:
    def __init__(self, fila, columna, capacidad):
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad
    
    def getFila(self):
        return self.fila 
    
    def getColumna(self):
        return self.columna 
        
    def getCapacidad(self):
        return self.capacidad

    def mostrar_unidad_militar(self):
        print("FILA: "+str(self.fila)+" COLUMNA: "+str(self.columna)+" CAPACIDAD: "+str(self.capacidad))