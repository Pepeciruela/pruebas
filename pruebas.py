simbolos = {"MMM":3000, "MM":2000, "M":1000, "D":500, "CCC":300, "CC":200, "C":100, "L":50, "XXX":30, "XX":20, "X":10, "V":5, "III":3, "II":2, "I":1}

def simbolo_a_entero(romano):
    if isinstance(romano, str) and romano.upper() in simbolos:
        return simbolos[romano.upper()]
    elif isinstance(romano, str):
        raise ValueError(f"simbolo {romano} no permitido")
    else:
        raise ValueError(f"parámetro {romano} debe ser un string")
    
def romano_a_entero(romano):
    for numero in range(len(romano)):
        #Letra actual y letra siguiente
        numero_actual = romano[numero]
        if numero != len(romano)-1: #Si existe una letra siguiente
            numero_siguiente = romano[numero+1]
        else: #Si es la última letra
            numero_siguiente = numero_actual
        # Si está seguido de una letra igual o menor
        if siguiente (numero_actual) >= siguiente (numero_siguiente):
            valor_siguiente += siguiente(numero_actual)
        #Si está seguido de un valor mayor
        elif siguiente (numero_actual) < siguiente (numero_siguiente):
            valor_siguiente -= siguiente (numero_actual)
    return valor_siguiente
        
print (romano_a_entero ("M"))