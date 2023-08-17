from ListaSimple import ListaEnlazada
from ListaDoble import ListaDoble
from ListaListas import Listalista
from ListaCircular import ListaCircular

#lista simple enlazada
lista = ListaEnlazada()
lista.agregar("Juan","Perez")
lista.agregar("Marcela","Diaz")
lista.imprimir()


#lista doble enlazada
listadoble = ListaDoble()
listadoble.agregar("Juan","Perez")
listadoble.agregar("Marcela","Diaz")
listadoble.agregar("Javier","Monjes")
listadoble.imprimir()

listaLista = Listalista()
listaLista.agregar("Juan","Perez")
numero = listaLista.primero
numero.lista.agregar("Carlos","Rodas")
numero.lista.agregar("Ana","Lopez")
listaLista.agregar("Diana","Calderon")


listaCircular = ListaCircular()
listaCircular.agregar(1)
listaCircular.agregar(2)
listaCircular.agregar(3)
listaCircular.agregar(4)
listaCircular.imprimir()