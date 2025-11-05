from Utilidades import digitos_de_numero #importamos la funcion para obtener los digitos de un numero

def suma_numeros_extremos(numero):
    digitos = digitos_de_numero(numero) #Obtenemos los digitos del numero y los almacenamos en una lista
    if len (digitos) == 0: #Si no hay digitos, retornamos 0
        return 0
    elif len(digitos) == 1: #Si solo hay un digito, retornamos ese digito
        return digitos[0] 
    else :
        suma = 0
        for i in range ((len(digitos))//2):#Leemos cuantos digitos hay y lo dividimos entre 2 para saber cuantas parejas de extremos hay que sumar
            suma += digitos[i] + digitos[-(i+1)]#Sumamos el digito de la posicion i y el digito de la posicion -i-1 (el extremo opuesto)
            suma_parcial = digitos[i] + digitos[-(i+1)]
            print(f"Sumando dígitos extremos: {digitos[i]} + {digitos[-(i+1)]} = {suma_parcial}", end=" | ", flush=True) #end para que no haga salto de linea y flush para que se muestre inmediatamente
        print() #Para hacer un salto de linea despues del bucle
        if len(digitos) % 2 != 0:#Si la cantidad de digitos es impar
            suma += digitos[len(digitos)//2]#Sumamos el digito del medio que no se ha sumado
        return suma