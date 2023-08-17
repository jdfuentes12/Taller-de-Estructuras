class Nodo:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.siguiente = None
        self.anterior = None
    
class ListaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self,nombre,apellido):
        nuevo_Nodo = Nodo(nombre,apellido)
        if not self.primero:
            self.primero = nuevo_Nodo
            self.ultimo = nuevo_Nodo
        else:
            nuevo_Nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_Nodo
            self.ultimo = nuevo_Nodo
        
    def imprimir(self):
        temp = self.primero
        while temp:
            print("El nombre es: ",temp.nombre," ",temp.apellido)
            temp = temp.siguiente
        print("None")