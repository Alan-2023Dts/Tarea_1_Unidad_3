def digitos_de_numero(numero):
    if numero < 0:
        numero = abs(numero)
    if numero != int(numero):
        raise ValueError("El número debe ser un entero.")
    else:
        numero = int(numero)
    return [int(digito) for digito in str(numero)]
# Usamos abs para manejar números negativos y cambiarlo a positivos y los almacenamos en una lista.

    
def limpiar_Consola():
    import os
    input("Presiona Enter para continuar...")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
def Mostrar_Titulo():
    
    print("╔" + "═" * 38 + "╗")
    print("║     Unidad_3_Tarea_1    ║")
    print("║              ¡Bienvenido!                ║")
    print("╚" + "═" * 38 + "╝")