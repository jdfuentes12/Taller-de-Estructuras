from ListaDoble import ListaDoble
from ListaSimple import ListaEnlazada
from Listalista import Listalistas
from ListaCircular import ListaCircular

lista_doble = ListaDoble()
lista_simple = ListaEnlazada()
lista_lista = Listalistas()
lista_circular = ListaCircular()

#lista simple
lista_simple.agregar(10)
lista_simple.agregar(11)
lista_simple.agregar(15)
lista_simple.imprimir()

#lista doble
lista_doble.insetar(15)
lista_doble.insetar(16)
lista_doble.insetar(17)
lista_doble.imprimir()

#lista de listas
lista_lista.agregar(2)
lista_lista.agregar(3)
lista_lista.agregar(4)
lista_lista.agregar(5)
numero = lista_lista.primero
numero.lista.agregar(1)
numero.lista.agregar(20)
numero.lista.agregar(50)

#lista circular
lista_circular.agregar(41)
lista_circular.agregar(42)
lista_circular.agregar(43)
lista_circular.imprimir()