class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.size = 0
    
    def agregar(self,dato):
        nuevo_Nodo = Nodo(dato)
        if not self.primero:
            self.primero = nuevo_Nodo
            nuevo_Nodo.siguiente = self.primero
            self.size = self.size + 1
        else:
            temp = self.primero
            while temp.siguiente != self.primero:
                temp = temp.siguiente
            temp.siguiente = nuevo_Nodo
            nuevo_Nodo.siguiente = self.primero
            self.size = self.size + 1
    
    def imprimir(self):
        if not self.primero:
            print("Lista vacia")
        temp = self.primero
        while True:
            print(temp.dato)
            temp = temp.siguiente
            if temp == self.primero:
                break
        print("None")

        