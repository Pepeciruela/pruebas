"""Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres por otro situado n posiciones más a la derecha. 
Si n = 2, por ejemplo, sustituiremos la <a> por la <c>, la <b> por la <e>, y así sucesivamente. El problema que aparece en las últimas n letras del alfabeto tiene fácil solución: en el ejemplo, la letra <y> se sustituirá por la <a> y la letra <z> por la <b>. La sustitución debe aplicarse a las letras minúsculas y mayúsculas y a los dígitos (el <0> se sustituye por el <2>, el <1> por el <3> y así hasta llegar al <9>, que se sustituye por el <1>).
Diseña un programa que lea un texto y el valor de n y muestre su versión criptografiada y la versión inversa, que dado un texto y la distancia lo descodifique.
Ten en cuenta los acentos y mayúsculas."""

def cifrado_letras():    
    letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    cambios = ("c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b")
    cifra = { letra: cifrada for letra, cifrada in zip(letras, cambios) }
        
    texto_entrada = input ("Introduce el texto a cifrar: ")
    
    texto_cifrado = "" 
    for letra in texto_entrada:
        if letra in cifra:
            texto_cifrado += cifra[letra]
        else:
            texto_cifrado += letra 
            
    return texto_cifrado

def cifrado_numeros():
    numeros = ("1","2","3","4","5","6","7","8","9","0")
    cambios = ("3","4","5","6","7","8","9","0","1","2")
    cifra = { numero: cifrada for numero, cifrada in zip(numeros, cambios) }
        
    numero_entrada = input ("Introduce los numeros a cifrar: ")
    
    numero_cifrado = "" 
    for numero in numero_entrada:
        if numero in cifra:
            numero_cifrado += cifra[numero]
        else:
            numero_cifrado += numero 
            
    return numero_cifrado
    
print (cifrado_letras())
print (cifrado_numeros())