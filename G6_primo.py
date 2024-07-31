# ----------------------------------------------------------------------------------------
# PROGRAMA: G6_primo.py
# ----------------------------------------------------------------------------------------
# Descripción: 
# Este programa verifica si un número natural dado es primo o no.
# Un número primo es aquel que solo es divisible por 1 y por sí mismo.
# El programa muestra si el número es primo o no.
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [30.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
# ----------------------------------------------------------------------------------------
import datetime   # modulo de python para este ejemplo (se usara para mostrar la fecha)
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES 
#----------------------------------------------------------------------------------------
# PRECONDICIONES
# ----------------------------------------------------------------------------------------
# 1. El Numero ingresado debe ser natural.
# ----------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------
#numero_in = Almacena el número ingresado por el usuario para su posterior validación
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# 1. El programa debe determinar si el número dado es primo o no.
# 2. El programa debe mostrar un mensaje indicando si el número es primo o no.
# 
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros
numero_in = int(input("Ingrese un número entero positivo: "))
# <<Escriba desde aqui el código del programa...>>
print(datetime.date.today())

def validaciones(numero):
    if numero < 0:
        print("El numero tiene que ser Natural")
        return False
    return True 

def primo(numero):
    """
    Función para determinar si un número es primo.
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if validaciones(numero_in):
    if primo(numero_in):
        print("El numero es primo")
    else: 
        print("El numero no es primo")    

# -------------------------------------------------------------------------------------            ---
# end.
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
    
