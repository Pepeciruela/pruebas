import collections

"""lista1 = ("MMCCMXL")
lista2 = list(lista1)

cuenta1 = collections.Counter(lista2)

print(lista2)
print(cuenta1)"""

def experimento (romano):
    lista_comprobacion = list(romano)
    contador_letras = collections.Counter(lista_comprobacion)
    for letra in contador_letras.values():
        if letra > 4:
            return OverflowError(F"Demasiados símbolos de tipo {letra}")
        elif letra > 3:
            return OverflowError(F"Demasiados símbolos de tipo {letra}")
    else:
        return True      
    
print(experimento("MMMCMXCIX")) 

