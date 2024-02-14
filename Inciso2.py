from Inciso1 import cadena_a_bits

def bytes_a_cadena(bits_lista):
    caracteres = []
    for bits in bits_lista:
        valor_decimal = int(bits, 2)
        caracteres.append(chr(valor_decimal))
    return ''.join(caracteres)



ejemplo_1 = cadena_a_bits("Cifrado")
ejemplo = bytes_a_cadena(ejemplo_1)
print(ejemplo)

ejemplo_2 = cadena_a_bits("Hola")
ejemplo_1 = bytes_a_cadena(ejemplo_2)
print(ejemplo_1)