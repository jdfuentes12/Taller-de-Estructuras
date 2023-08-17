class Node:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None

    def agregar(self, data):
        nuevo_nodo = Node(data)
        if not self.primero:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            aux = self.primero
            while aux.siguiente != self.primero:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def imprimir(self):
        if not self.primero:
            print("No hay elementos en la lista")
            return
        aux = self.primero
        while True:
            print(aux.data)
            aux = aux.siguiente
            if aux == self.primero:
                break
        print(self.primero.data)  

