class Fila:
    def __init__(self, numero, lista):
        self.numero = numero
        self.lista = lista

    def getNumero(self):
        return self.numero
    def getLista(self):
        return self.lista 
    def mostrar_fila(self):
        print("NUMERO: "+str(self.numero)+" FILA: "+str(self.lista))
