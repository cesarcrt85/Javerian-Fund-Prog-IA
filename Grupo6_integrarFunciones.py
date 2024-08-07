# ----------------------------------------------------------------------------------------
# PROGRAMA: Grupo6_integrarFunciones.py
# ----------------------------------------------------------------------------------------
# Descripción: 
# Este programa tiene como objetivo implementar un conjunto de funciones para resolver las
# siguientes tareas: crear dos listas de 10 valores enteros cada una, donde la primera 
# lista, denominada listaUno, debe ser generada de manera aleatoria, y la segunda lista, 
# denominada listaDos, se debe generar a partir de 10 valores enteros que serán pedidos al 
# usuario uno por uno. Además, se crearán dos listas inicialmente vacías: listaClonada y 
# listaSuma. El programa principal presentará un menú con opciones para llevar a cabo 
# diferentes tareas indicadas.
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [07.08.2024]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import random
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES 
#-----------------------------------------------------------------------------------------
#listaClonada: Almacena la lista cloda resultante de la funcion clonarLista
#listaSuma: Almacena la lista resultante de la suma de la lista uno y lista dos
#listaUno: Almacena 10 valores enteros generados aleatoreamente
#listaDos: Almacena 10 valores enteros ingresados por el usuario
#----------------------------------------------------------------------------------------
# PRECONDICIONES
# ----------------------------------------------------------------------------------------
#1. El usuario debe ingresar 10 valores enteros para llenar la lista dos
#2. El usuario debe seleccionar la opción de un menú para que el sistema realice una acción 
#------------------------------------------------------------------------------------------
# POSTCONDICIONES
#------------------------------------------------------------------------------------------
#1. El sistema debe realizar las operaciones indicadas por el usuario según la opción que haya 
#seleccionado
#2. El sistema debe mostrar el resultado de la función ejecutada según la selección del usuario
# --------------------------

# Función para generar una lista aleatoria de tamaño n
def listaAleatoria(n):
    return [random.randint(1, 100) for _ in range(n)]

# Función para generar una lista ingresada por el usuario de tamaño n
def listaManual(n):
    lista = []
    print("A continuacin ingresará los ", n, " valores de la lista dos:")
    for i in range(n):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        lista.append(valor)
    return lista

# Función para mostrar los valores de listaUno y listaDos
def mostrarLista(listaUno, listaDos):
    print("Los valores de listaUno son:")
    for valor in listaUno:
        print(valor)
        
    print("Los valores de listaDos son:")
    for valor in listaDos:
        print(valor)

# Función para mostrar el valor máximo y mínimo de la lista uno
def minMax(listaUno):

    max_value = max(listaUno)
    min_value = min(listaUno)
    return max_value, min_value
    

# Función para clonar una lista
def clonarLista(lista):
    return lista.copy()

# Función para sumar dos listas elemento a elemento
def sumarListas(lista1, lista2):
    return [x + y for x, y in zip(lista1, lista2)]

# Función para determinar si un elemento está en la lista suma
def valorEnLista(listaSuma, k):
    return k in listaSuma
 # Mostrar el menú y realizar las tareas indicadas
def mostrarMenu(listaSuma):
        print("*********************************************************************")
        print("----- MENÚ -----")
        print("0. Salir")
        print("1. Mostrar Valores (listaUno y listaDos")
        print("2. Valor Máximo y Mínimo (listaUno)")
        print("3. Clonar listaUno")
        print("4. Sumar Listas (listaClonada y listaDos)")
        print("5. ¿Valor en lista? (listaSuma)")
        print("*********************************************************************")
        
        opcion = int(input("\nIngrese la opción deseada (1-5) o 0 para terminar:"))
        
        if opcion == 0:
            print("Finalizando del programa...")
            
        elif opcion == 1:
            mostrarLista(listaUno, listaDos)
            mostrarMenu(listaSuma)
        elif opcion == 2:
            max_value, min_value =minMax(listaUno)
            print("El valor máximo de la lista es:", max_value)
            print("El valor mínimo de la lista es:", min_value)
            mostrarMenu(listaSuma)
        elif opcion == 3:
            listaClonada = clonarLista(listaUno)
            print("Lista clonada:", listaClonada)
            mostrarMenu(listaSuma)
        elif opcion == 4:
            listaSuma = sumarListas(listaUno, listaDos)
            print("Lista suma:", listaSuma)
            mostrarMenu(listaSuma)
        elif opcion == 5:
            k = int(input("Ingrese el valor que desea buscar en la listaSuma: "))
            if valorEnLista(listaSuma,k)==True :
                print("El valor ",k," si se encuentra en ListaSuma")
            else:
                print("El valor ",k," no se encuentra en ListaSuma")       
            mostrarMenu(listaSuma)
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.") 
            mostrarMenu(listaSuma)
            
# Crear las listas listaClonada y listaSuma
listaClonada = []
listaSuma = []

# Crear las listas listaUno y listaDos
listaUno = listaAleatoria(10)
listaDos = listaManual(10)
    
mostrarMenu(listaSuma)
    
print("Fin del programa.")
# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
