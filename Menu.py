from Ecuaciones_Simultaneas import resolver_sistema
from Suma_numeros_Extremos import suma_numeros_extremos
from Utilidades import limpiar_Consola

#Mostrar el menu (solo es texto)
def menu():
    print("Seleccione una opción:")
    print("1. Sistema de ecuaciones")
    print("2. Sumar los dígitos extremos de un número")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")
    limpiar_Consola()
    return opcion

def procesar_opcion(opcion):
    
    if opcion == '1':
        #Sistema de ecuaciones
        print("Resolución de un sistema de ecuaciones lineales de la forma:")
        print("a·x + b·y = c")
        print("p·x + q·y = r")
        #Entrada de datos
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        p = float(input("Ingrese el valor de p: "))
        q = float(input("Ingrese el valor de q: "))
        r = float(input("Ingrese el valor de r: "))
        #Resolucion del sistema
        tiene_solucionn_unica, x, y = resolver_sistema(a, b, c, p, q, r)
        if tiene_solucionn_unica:
            print(f"La solución única es: x = {x}, y = {y}")
            limpiar_Consola()
        else:
            print("El sistema no tiene solución única.")
            limpiar_Consola()
            
            #Suma de digitos extremos
    elif opcion == '2':
        #entrada de datos
        numero = int(input("Ingrese un número entero: "))
        resultado = suma_numeros_extremos(numero)
        print(f"La suma de los dígitos extremos es: {resultado}")
        limpiar_Consola()
        #Salir del programa
    elif opcion == '3':
        print("Saliendo del programa...")
        limpiar_Consola()
    else:
        #Opción no válida
        print("Opción no válida. Por favor, intente de nuevo.")
        limpiar_Consola()