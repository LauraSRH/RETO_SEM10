#Reto semana 10, dos listas.
#Emplear funciones para:
# Que permita crear dos listas de distintas longitudes.
# Que la longitud y los elementos de cada lista sean especificados por el usuario.
# Que imprima las listas indicando que son las listas originales.
# Que elimine de la primera lista los nombres de la segunda.
# Que imprima la primera lista indicando que se han eliminado los elementos que
# estaban también en la segunda.

def crear_lista(nombres_lista):
    """Pregunta cuantos elementos se ingresaran a la lista.
    Crea la lista de elementos especificada por el usuario 
    con el numero de elementos a ingresar."""
    lista =[]
    longitud = int(input(f"¿Cuántos elementos tendrá la {nombres_lista}? "))
    for i in range(longitud):
        elemento = input(f"Introduce el elemento {i+1} de la {nombres_lista}: ")
        lista.append(elemento)
    return lista

def eliminar_elementos(lista1, lista2):
    """Elimina de la primera lista los elementos que están en la segunda lista."""
    return [elemento for elemento in lista1 if elemento not in lista2]

lista1 = crear_lista("primera lista")
lista2 = crear_lista("segunda lista")
print("Lista original 1:", lista1)
print("Lista original 2:", lista2)

lista1 = eliminar_elementos(lista1, lista2)
print("Lista 1 después de eliminar elementos de la lista 2:", lista1)
#Ejercicio adicional del reto semana 10.