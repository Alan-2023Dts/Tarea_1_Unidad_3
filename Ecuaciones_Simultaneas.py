def resolver_sistema(a,b,c,p,q,r):

    #Validacion de que los parametros sean numericos Propuesta por copilot
    #######################################
    #Validacion de que los parametros sean numericos
    from numbers import Real#Esto funciona para hacer la validacion de tipos numericos
    for name, val in (('a', a), ('b', b), ('c', c), ('p', p), ('q', q), ('r', r)): #Iteramos sobre los parametros para validar su tipo
        if not isinstance(val, Real): #Si el parametro no es numerico
            raise TypeError(f"Parámetro {name} debe ser numérico (int o float), no {type(val).__name__}") #Lanzamos un error de tipo con un mensaje descriptivo
    ####################################### 
    
    #Usare el metodo de determinantes de cramer
    # Calculamos el determinante del sistema
    tiene_solucionn_unica = True
    Determinante  = a*q - p*b
    if Determinante != 0:
        #Dx = c·q − b·r
        Dx = c*q - b*r
        #Dy = a·r − c·p
        Dy = a*r - c*p
        x = Dx / Determinante
        y = Dy / Determinante
        return (tiene_solucionn_unica,x, y) #Devolvemos true y las soluciones
    else:
        tiene_solucionn_unica = False
        return (tiene_solucionn_unica, None, None)  # El none funciona como indicador de que no hay solución única (devuelve nada)
