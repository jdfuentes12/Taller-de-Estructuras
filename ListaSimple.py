class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente
        print("None")

    def primero(self):
        tmp = self.primero
        return tmp
