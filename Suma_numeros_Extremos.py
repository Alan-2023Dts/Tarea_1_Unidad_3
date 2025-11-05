from Utilidades import digitos_de_numero

def suma_numeros_extremos(numero):
    digitos = digitos_de_numero(numero)
    if len (digitos) == 0:
        return 0
    elif len(digitos) == 1:
        return digitos[0] 
    else :
        suma = 0
        for i in range ((len(digitos))//2):#Leemos cuantos digitos hay y lo dividimos entre 2 para saber cuantas parejas de extremos hay que sumar
            suma += digitos[i] + digitos[-(i+1)]#Sumamos el digito de la posicion i y el digito de la posicion -i-1 (el extremo opuesto)
        if len(digitos) % 2 != 0:#Si la cantidad de digitos es impar
            suma += digitos[len(digitos)//2]#Sumamos el digito del medio que no se ha sumado
        return suma