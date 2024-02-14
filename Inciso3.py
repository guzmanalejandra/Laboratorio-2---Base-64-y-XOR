import base64

def convert_to_base64(string):

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    binary_string = ''.join(format(ord(char), '08b') for char in string)

    while len(binary_string) % 6 != 0:
        binary_string += '0'

    base64_string = ''
    for i in range(0, len(binary_string), 6):
        index = int(binary_string[i:i+6], 2)
        base64_string += base64_chars[index]

    return base64_string
import base64

def string_to_binary(string):
    binary = ''.join(format(ord(char), '08b') for char in string)
    return binary

def binary_to_base64(binary):
    base64_encoded = base64.b64encode(binary.encode()).decode()
    return base64_encoded


ejemplo1 = "Hola"
binary1 = string_to_binary(ejemplo1)
base64_1 = binary_to_base64(binary1)
print(f"Base 64 ejemplo 1: {base64_1}")


ejemplo2 = "Cifrado"
binary2 = string_to_binary(ejemplo2)
base64_2 = binary_to_base64(binary2)
print(f"Base 64 ejemplo 2: {base64_2}")


def convertir_a_base64(cadena):
    binario = ''.join(format(ord(caracter), '08b') for caracter in cadena)
    resultado_base64 = base64.b64encode(binario.encode('utf-8')).decode('utf-8')
    return resultado_base64

cadena1 = "Hola, mundo!"
cadena2 = "¡Hola a todos!"

resultado1 = convertir_a_base64(cadena1)
resultado2 = convertir_a_base64(cadena2)

print(resultado1)
print(resultado2)