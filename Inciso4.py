
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_a_texto(base64):
    base64 = base64.rstrip('=')
    bits = ''
    for char in base64:
        if char in BASE64_CHARS:
            bits += bin(BASE64_CHARS.index(char))[2:].zfill(6)
    bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]
    texto = ''
    for byte in bytes_list:
        texto += chr(int(byte, 2))
    
    return texto


base64_ejemplo_1 = "Q2lmcmFkbw=="  # Cifrado
print(base64_a_texto(base64_ejemplo_1))

base64_ejemplo_2 = "SG9sYQ=="  # Hola
print(base64_a_texto(base64_ejemplo_2))
