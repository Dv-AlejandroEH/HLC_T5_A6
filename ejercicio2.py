import random

def imprimir_caracteres(longitud):
    contraseña = ''
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?'
    for i in range(longitud):
        numero_random = random.randint(0, len(caracteres)-1)
        caracter_random = caracteres[numero_random]
        contraseña += caracter_random
    return contraseña
print(imprimir_caracteres(100))