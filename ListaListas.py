from ListaSimple import ListaEnlazada

class Nodo:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.lista = ListaEnlazada()
        self.siguiente = None

class Listalista:
    def __init__(self):
        self.primero = None

    def agregar(self,nombre,apllido):
        nuevo_Nodo = Nodo(nombre,apllido)
        if self.primero is None:
            self.primero = nuevo_Nodo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo_Nodo
    
    def imprimir(self):
        temp = self.primero
        while temp:
            print("El nombre es: ",temp.nombre," ",temp.apellido)
            temp = temp.siguiente
        print("None")

    def buscar(self,id):
        temp = self.primero
        while temp:
            if temp.id == id:
                return temp
            temp = temp.siguiente
        return temp