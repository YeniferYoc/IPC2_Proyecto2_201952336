
class Robot:
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        
    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo
    
    def getCapacidad(self):
        return self.capacidad 

    def mostrar_robot(self):
        print("NOMBRE:  "+str(self.nombre)+" TIPO: "+str(self.tipo)+" CAPACIDAD: "+str(self.capacidad))