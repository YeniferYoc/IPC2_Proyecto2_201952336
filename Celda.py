class Celda:
    def __init__(self, fila, columna, tipo):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def getFila(self):
        return self.fila
    def getColumna(self):
        return self.columna
    def getTipo(self):
        return self.tipo  
    def mostrar_celda(self):
        print("FILA: "+str(self.fila)+" COLUMNA: "+str(self.columna)+" TIPO: "+str(self.tipo))
