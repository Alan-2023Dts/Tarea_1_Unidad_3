from Ecuaciones_Simultaneas import resolver_sistema_ecuaciones
from Suma_numeros_Extremos import suma_numeros_extremos
def menu():
    print("Seleccione una opción:")
    print("1. Sistema de ecuaciones")
    print("2. Sumar los dígitos extremos de un número")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

def procesar_opcion(opcion):
    if opcion == '1':
        resolver_sistema_ecuaciones()
    elif opcion == '2':
        numero = int(input("Ingrese un número entero: "))
        resultado = suma_numeros_extremos(numero)
        print(f"La suma de los dígitos extremos es: {resultado}")
    elif opcion == '3':
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")