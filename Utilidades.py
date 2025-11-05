def digitos_de_numero(numero):
    if numero < 0:
        numero = abs(numero)
    if numero != int(numero):
        raise ValueError("El número debe ser un entero.")
    else:
        numero = int(numero)
    return [int(digito) for digito in str(numero)]
# Usamos abs para manejar números negativos y cambiarlo a positivos y los almacenamos en una lista.

    