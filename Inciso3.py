
from Inciso1 import cadena_a_bits

BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def cadena_a_base64(cadena):

    bits = ''.join(cadena_a_bits(cadena))
    bloques_6_bits = [bits[i:i+6] for i in range(0, len(bits), 6)]
    base64 = ''
    for bloque in bloques_6_bits:
        if len(bloque) < 6:
            bloque += '0' * (6 - len(bloque))  
        indice = int(bloque, 2)
        base64 += BASE64_CHARS[indice]
    
    
    while len(base64) % 4 != 0:
        base64 += '='
    
    return base64

print(cadena_a_base64("Cifrado"))  
print(cadena_a_base64("Hola"))    
