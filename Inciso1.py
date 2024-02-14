def cadena_a_bits(cadena):
    resultado_bits = []
    for caracter in cadena:
        bits = bin(ord(caracter))[2:].zfill(8)
        resultado_bits.append(bits)
    return resultado_bits

#Ejemplo de uso 1
ejemplo_1 = cadena_a_bits("Cifrado")
print(ejemplo_1)

#RESULTADO EN INTERNET: 01000011 01101001 01100110 01110010 01100001 01100100 01101111 
#Ejemplo de uso 2

ejemplo_2 = cadena_a_bits("Hola")
print(ejemplo_2)

#RESULTADO EN INTERNET: 01001000 01101111 01101100 01100001 