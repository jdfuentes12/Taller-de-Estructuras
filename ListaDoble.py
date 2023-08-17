class Node:
    def __init__(self, data):
        self.data = data
        self.anterior = None
        self.despues = None

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insetar(self, data):
        new_node = Node(data)
        if not self.primero:
            self.primero = new_node
            self.ultimo = new_node
        else:
            new_node.anterior = self.ultimo
            self.ultimo.despues = new_node
            self.ultimo = new_node

    def imprimir(self):
        current = self.primero
        while current:
            print(current.data)
            current = current.despues
        print("None")