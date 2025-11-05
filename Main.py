from Menu import menu, procesar_opcion
from Utilidades import limpiar_Consola,Mostrar_Titulo 

def main():
    
    Mostrar_Titulo() #Mostrar el titulo de la aplicacion
    limpiar_Consola()
    #Bucle principal del programa
    while True:

        
        opcion = menu() #Mostrar el menu y obtener la opcion del usuario
        if opcion == '3': #Salir del programa
            break
        procesar_opcion(opcion)

if __name__ == "__main__":
    main()