class Nodo:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.siguiente = None

class ListaEnlazada():
    def __init__(self):
        self.primero = None

    def agregar(self, nombre, apellido):
        nuevo_nodo = Nodo(nombre,apellido)
        if self.primero == None:
            self.primero = nuevo_nodo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
    
    def imprimir(self):
        temp = self.primero
        while temp:
            print("El nombre es: ",temp.nombre," ",temp.apellido)
            temp = temp.siguiente
        print("None")