from Fila import *
class Ciudad:
    def __init__(self, nombre, cant_filas, cant_columnas, filas):
        self.nombre = nombre
        self.cant_filas = cant_filas
        self.cant_columnas = cant_columnas
        self.filas = filas
        
    def getNombre(self):
        return self.nombre
    
    def getCant_filas(self):
        return self.cant_filas 
    
    def getCant_columnas(self):
        return self.cant_columnas 
        
    def getFilas(self):
        return self.filas

    def mostrar_ciudad(self):
        print("NOMBRE:  "+str(self.nombre)+" CANTIDAD DE FILAS: "+str(self.cant_filas)+" CANTIDAD DE COLUMNAS: "+str(self.cant_columnas))
        for fila in self.filas: 
            fila.mostrar_fila()