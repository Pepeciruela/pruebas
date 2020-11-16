simbolos = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}


def simbolo_a_entero(romano):
    cadena = []
    descomponer = list(romano)
    cadena.append(descomponer)
    return cadena

def romano_a_entero(romano):
    valores = []
    letras = simbolo_a_entero(romano)
    for letra in letras:
        if romano in simbolos:
            valores.append(simbolos[romano.upper()])
    return valores

print (simbolo_a_entero ("MMM"))
print (romano_a_entero ("MM"))
